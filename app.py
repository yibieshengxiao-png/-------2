# 冠之今天吃什么 - Flask 主程序
# 冰箱食谱生成器，输入食材一键生成多套食谱方案

import json
import os
from flask import Flask, render_template, request, jsonify, send_from_directory

from data_ingredients import INGREDIENTS, VISIBLE_INGREDIENTS, BASIC_SEASONINGS, CATEGORY_ORDER, ALL_TAGS
from data_recipes import RECIPES

app = Flask(__name__)
app.secret_key = "guanzhi_recipe_secret"

ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")


def attach_icons():
    """为食材和食谱附加 icon 图片路径；无图标则为空字符串，前端回退到 emoji。"""
    for ing in INGREDIENTS:
        fname = f"ing_{ing['id']}.png"
        ing["icon"] = f"/icons/{fname}" if os.path.exists(os.path.join(ICON_DIR, fname)) else ""
    for r in RECIPES:
        fname = f"recipe_{r['id']}.png"
        r["icon"] = f"/icons/{fname}" if os.path.exists(os.path.join(ICON_DIR, fname)) else ""


attach_icons()


@app.route("/icons/<path:filename>")
def serve_icon(filename):
    """提供食材/食谱图标静态资源"""
    return send_from_directory(ICON_DIR, filename)


# ============================================================
# 辅助函数
# ============================================================

def get_ingredient_by_name(name):
    """根据名称查找食材"""
    for ing in INGREDIENTS:
        if ing["name"] == name:
            return ing
    return None


def get_ingredient_by_id(ing_id):
    """根据 ID 查找食材"""
    for ing in INGREDIENTS:
        if ing["id"] == ing_id:
            return ing
    return None


def build_recipe_result(recipe, missing_items, insufficient_items, available_items, match_ratio):
    """构建单个食谱的结果字典"""
    calories = recipe.get("nutrition", {}).get("calories", 300)
    salt = recipe.get("nutrition", {}).get("salt", 2.0)
    health_stars = recipe.get("healthStars", 3)
    star_str = "★" * health_stars + "☆" * (5 - health_stars)
    diet_friendly = recipe.get("dietFriendly", False)

    if salt <= 1.5:
        salt_level = "green"
    elif salt <= 3.0:
        salt_level = "yellow"
    else:
        salt_level = "red"

    if calories <= 200:
        cal_level = "green"
    elif calories <= 400:
        cal_level = "yellow"
    else:
        cal_level = "red"

    if len(missing_items) == 0 and len(insufficient_items) == 0:
        status = "green"
        status_text = "可直接做"
    elif len(missing_items) == 0 and len(insufficient_items) > 0:
        status = "yellow"
        status_text = "食材不够"
    else:
        status = "red"
        status_text = f"缺 {len(missing_items)} 样"

    return {
        "id": recipe["id"],
        "name": recipe["name"],
        "category": recipe["category"],
        "description": recipe["description"],
        "emoji": recipe["emoji"],
        "icon": recipe.get("icon", ""),
        "prepTime": recipe["prepTime"],
        "cookTime": recipe["cookTime"],
        "totalTime": recipe["prepTime"] + recipe["cookTime"],
        "ingredients": recipe["ingredients"],
        "seasonings": recipe["seasonings"],
        "steps": recipe["steps"],
        "tags": recipe.get("tags", []),
        "calories": calories,
        "salt": salt,
        "healthStars": health_stars,
        "starStr": star_str,
        "dietFriendly": diet_friendly,
        "dietNote": recipe.get("dietNote", ""),
        "saltLevel": salt_level,
        "calLevel": cal_level,
        "status": status,
        "statusText": status_text,
        "matchRatio": match_ratio,
        "missingItems": missing_items,
        "insufficientItems": insufficient_items,
        "availableItems": available_items,
        "missingCount": len(missing_items),
        "insufficientCount": len(insufficient_items),
    }


def match_recipes(selected_items, servings=2):
    """
    核心匹配引擎：根据用户选择的食材匹配食谱库。
    selected_items: [{"id": "v001", "amount": 300}, ...]
    servings: 用餐份数（人数×顿数），默认2人份，食谱用量按比例缩放
    返回: 排序后的食谱列表，每道菜附带食材状态。
    """
    if not selected_items or len(selected_items) == 0:
        return []

    # 每道食谱默认2人份，按实际份数缩放
    DEFAULT_SERVING = 2
    scale = servings / DEFAULT_SERVING

    # 构建用户食材字典: {name: amount_g}
    user_ingredients = {}
    for item in selected_items:
        ing = get_ingredient_by_id(item["id"])
        if ing:
            amount = item.get("amount", 0)
            user_ingredients[ing["name"]] = {
                "amount": amount,
                "ingredient": ing,
            }

    results = []

    for recipe in RECIPES:
        missing_items = []
        insufficient_items = []
        available_items = []
        total_required = 0
        matched_amount = 0
        overlap_count = 0  # 用户食材与食谱食材的重合数

        for ri in recipe["ingredients"]:
            name = ri["name"]

            if name in BASIC_SEASONINGS:
                available_items.append({
                    "name": name, "needed": f"{ri['amount']}{ri['unit']}",
                    "status": "auto", "existing": "已有",
                })
                continue

            total_required += 1  # 只统计主要食材

            if name in user_ingredients:
                overlap_count += 1
                user_amt = user_ingredients[name]["amount"]
                needed_amt = ri["amount"] * scale

                if user_amt >= needed_amt:
                    available_items.append({
                        "name": name, "needed": f"{needed_amt}{ri['unit']}",
                        "status": "ok", "existing": f"冰箱有 {user_amt}{ri['unit']}",
                    })
                    matched_amount += 1
                else:
                    insufficient_items.append({
                        "name": name, "needed": f"{needed_amt}{ri['unit']}",
                        "status": "insufficient",
                        "existing": f"冰箱仅 {user_amt}{ri['unit']}",
                        "shortage": needed_amt - user_amt,
                    })
            else:
                missing_items.append({
                    "name": name, "needed": f"{ri['amount']}{ri['unit']}",
                    "status": "missing",
                    "suggestion": suggest_replacement(name),
                })

        match_ratio = matched_amount / max(total_required, 1)
        result = build_recipe_result(recipe, missing_items, insufficient_items, available_items, match_ratio)
        result["overlapCount"] = overlap_count
        results.append(result)

    # 分离：有重合的（green + yellow + red with overlap）vs 无重合的
    with_overlap = [r for r in results if r["overlapCount"] > 0]
    no_overlap = [r for r in results if r["overlapCount"] == 0]

    # 统计各状态数量
    green_count = sum(1 for r in results if r["status"] == "green")
    yellow_count = sum(1 for r in results if r["status"] == "yellow")

    status_order = {"green": 0, "yellow": 1, "red": 2}
    # 排序：绿色优先 → 重合食材越多越靠前 → 匹配率高 → 缺的少
    with_overlap.sort(key=lambda r: (
        status_order.get(r["status"], 3),
        -r["overlapCount"],       # 重合食材越多越靠前
        -r["matchRatio"],
        r["missingCount"],
    ))

    # 无重合的按食谱名排序
    no_overlap.sort(key=lambda r: r["name"])

    # 判断标准：有可直接做的(green)或有食材不够的(yellow)才算"有匹配"
    has_good_match = green_count > 0 or yellow_count > 0

    return {
        "recipes": with_overlap + no_overlap,
        "totalCount": len(results),
        "matchedCount": len(with_overlap),
        "hasGoodMatch": has_good_match,
        "greenCount": green_count,
        "yellowCount": yellow_count,
    }


def suggest_replacement(name):
    """为缺的食材提供替换建议"""
    suggestions = {
        "猪肉": "可用鸡胸肉或牛肉替代",
        "猪里脊": "可用鸡胸肉替代，口感略不同",
        "五花肉": "可用猪腿肉替代，减少脂肪",
        "鸡胸肉": "可用猪里脊替代",
        "牛肉": "可用猪肉替代",
        "虾仁": "可用鸡胸肉丁替代",
        "鱼": "可用鸡腿肉替代",
        "豆腐": "可用豆干或豆皮替代",
        "老豆腐": "可用嫩豆腐替代",
        "木耳": "可用蘑菇替代",
        "青椒": "可用红椒或芹菜替代",
        "胡萝卜": "可用南瓜替代",
        "黄瓜": "可用西葫芦替代",
        "土豆": "可用山药或莲藕替代",
        "番茄": "可用番茄酱+少量糖替代",
        "鸡蛋": "一般不可替代",
        "葱": "可用洋葱替代",
        "大蒜": "可用姜替代（风味不同）",
        "生姜": "可用少量料酒替代去腥",
        "西兰花": "可用菜花替代",
        "菠菜": "可用生菜或白菜替代",
        "豆芽": "可用白菜丝替代",
        "四季豆": "可用豇豆替代",
        "茄子": "可用西葫芦替代",
    }
    return suggestions.get(name, "可用其他类似食材替代")


# ============================================================
# 路由
# ============================================================

@app.route("/")
def index():
    """主页面"""
    return render_template(
        "index.html",
        ingredients=VISIBLE_INGREDIENTS,
        categories=CATEGORY_ORDER,
        all_tags=ALL_TAGS,
        all_recipes=RECIPES,
        basic_seasonings=BASIC_SEASONINGS,
    )


@app.route("/api/generate", methods=["POST"])
def api_generate():
    """食谱生成 API"""
    data = request.get_json()
    if not data or "ingredients" not in data:
        return jsonify({"error": "请提供食材列表"}), 400

    selected = data["ingredients"]
    servings = data.get("servings", 2)  # 默认2人份
    results = match_recipes(selected, servings)
    return jsonify(results)


@app.route("/api/explore")
def api_explore():
    """探索 API：返回全部食谱（可按标签筛选）"""
    tag = request.args.get("tag", "")
    recipes = RECIPES

    if tag:
        recipes = [r for r in recipes if tag in r.get("tags", [])]

    # 返回简化版食谱数据
    result = []
    for r in recipes:
        calories = r.get("nutrition", {}).get("calories", 300)
        salt = r.get("nutrition", {}).get("salt", 2.0)
        health_stars = r.get("healthStars", 3)
        star_str = "★" * health_stars + "☆" * (5 - health_stars)
        diet_friendly = r.get("dietFriendly", False)

        if salt <= 1.5:
            salt_level = "green"
        elif salt <= 3.0:
            salt_level = "yellow"
        else:
            salt_level = "red"

        if calories <= 200:
            cal_level = "green"
        elif calories <= 400:
            cal_level = "yellow"
        else:
            cal_level = "red"

        result.append({
            "id": r["id"],
            "name": r["name"],
            "category": r["category"],
            "description": r["description"],
            "emoji": r["emoji"],
            "icon": r.get("icon", ""),
            "prepTime": r["prepTime"],
            "cookTime": r["cookTime"],
            "totalTime": r["prepTime"] + r["cookTime"],
            "ingredients": r["ingredients"],
            "seasonings": r["seasonings"],
            "steps": r["steps"],
            "tags": r.get("tags", []),
            "calories": calories,
            "salt": salt,
            "healthStars": health_stars,
            "starStr": star_str,
            "dietFriendly": diet_friendly,
            "dietNote": r.get("dietNote", ""),
            "saltLevel": salt_level,
            "calLevel": cal_level,
            "totalTime": r["prepTime"] + r["cookTime"],
        })

    return jsonify({
        "total": len(result),
        "recipes": result,
    })


@app.route("/api/recipes")
def api_recipes():
    """返回食谱库摘要"""
    summary = [{
        "id": r["id"],
        "name": r["name"],
        "category": r["category"],
        "description": r["description"],
        "emoji": r["emoji"],
        "tags": r.get("tags", []),
    } for r in RECIPES]
    return jsonify({
        "total": len(RECIPES),
        "recipes": summary,
    })


# ============================================================
# 启动
# ============================================================

if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    print("=" * 50)
    print("   [冠之今天吃什么] - 冰箱食谱生成器")
    print(f"   可选食材: {len(VISIBLE_INGREDIENTS)} 种  |  食谱库: {len(RECIPES)} 道家常菜")
    print("=" * 50)
    print()
    print("   打开浏览器访问: http://127.0.0.1:5000")
    print("   按 Ctrl+C 停止服务器")
    print()
    app.run(debug=True, host="0.0.0.0", port=5000)
