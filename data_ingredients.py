# 冰箱食材库 - 冠之今天吃什么
# 分类：蔬菜 / 肉蛋 / 豆制品 / 主食
# 每种食材包含：名称、分类、Emoji、单位、预置克重档位、每100g营养数据

INGREDIENTS = [
    # ===== 蔬菜类 =====
    {"id": "v001", "name": "青椒",  "category": "蔬菜", "emoji": "🫑",   "unit": "g",  "presets": [100, 200, 300, 500], "nutrition": {"calories": 20, "salt": 0.003}},
    {"id": "v002", "name": "红椒",  "category": "蔬菜", "emoji": "🌶️",  "unit": "g",  "presets": [100, 200, 300],       "nutrition": {"calories": 26, "salt": 0.002}},
    {"id": "v003", "name": "番茄",  "category": "蔬菜", "emoji": "🍅",   "unit": "g",  "presets": [150, 300, 450, 600],  "weightNote": "约150g/个", "nutrition": {"calories": 18, "salt": 0.005}},
    {"id": "v004", "name": "土豆",  "category": "蔬菜", "emoji": "🥔",   "unit": "g",  "presets": [200, 400, 600, 1000], "weightNote": "约200g/个", "nutrition": {"calories": 77, "salt": 0.003}},
    {"id": "v005", "name": "胡萝卜","category": "蔬菜", "emoji": "🥕",   "unit": "g",  "presets": [100, 200, 300],       "nutrition": {"calories": 41, "salt": 0.07}},
    {"id": "v006", "name": "白菜",  "category": "蔬菜", "emoji": "🥬",   "unit": "g",  "presets": [200, 300, 500, 1000], "nutrition": {"calories": 13, "salt": 0.05}},
    {"id": "v007", "name": "黄瓜",  "category": "蔬菜", "emoji": "🥒",   "unit": "g",  "presets": [200, 400, 600],       "weightNote": "约200g/根", "nutrition": {"calories": 15, "salt": 0.003}},
    {"id": "v008", "name": "茄子",  "category": "蔬菜", "emoji": "🍆",   "unit": "g",  "presets": [250, 500, 750],       "weightNote": "约250g/根", "nutrition": {"calories": 21, "salt": 0.004}},
    {"id": "v009", "name": "洋葱",  "category": "蔬菜", "emoji": "🧅",   "unit": "g",  "presets": [200, 400, 600],       "weightNote": "约200g/个", "nutrition": {"calories": 40, "salt": 0.004}},
    {"id": "v010", "name": "大蒜",  "category": "蔬菜", "emoji": "🧄",   "unit": "g",  "presets": [10, 30, 50],           "nutrition": {"calories": 149, "salt": 0.017}, "default": True},
    {"id": "v011", "name": "生姜",  "category": "蔬菜", "emoji": "🫚",   "unit": "g",  "presets": [10, 30, 50],           "nutrition": {"calories": 80, "salt": 0.013},  "default": True},
    {"id": "v012", "name": "葱",    "category": "蔬菜", "emoji": "🌿",   "unit": "g",  "presets": [10, 30, 50],           "nutrition": {"calories": 32, "salt": 0.005},  "default": True},
    {"id": "v013", "name": "西兰花","category": "蔬菜", "emoji": "🥦",   "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 34, "salt": 0.03}},
    {"id": "v014", "name": "菠菜",  "category": "蔬菜", "emoji": "🥗",   "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 23, "salt": 0.08}},
    {"id": "v015", "name": "四季豆","category": "蔬菜", "emoji": "🫘",   "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 31, "salt": 0.002}},
    {"id": "v016", "name": "豆芽",  "category": "蔬菜", "emoji": "🌱",   "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 18, "salt": 0.007}},
    {"id": "v017", "name": "韭菜",  "category": "蔬菜", "emoji": "🥬",   "unit": "g",  "presets": [100, 200, 300],       "nutrition": {"calories": 26, "salt": 0.002}},
    {"id": "v018", "name": "芹菜",  "category": "蔬菜", "emoji": "🌿",   "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 14, "salt": 0.08}},
    {"id": "v019", "name": "生菜",  "category": "蔬菜", "emoji": "🥬",   "unit": "g",  "presets": [100, 200, 300],       "nutrition": {"calories": 13, "salt": 0.02}},
    {"id": "v020", "name": "玉米",  "category": "蔬菜", "emoji": "🌽",   "unit": "g",  "presets": [250, 500, 750],       "weightNote": "约250g/根", "nutrition": {"calories": 112, "salt": 0.001}},
    {"id": "v021", "name": "冬瓜",  "category": "蔬菜", "emoji": "🍈",   "unit": "g",  "presets": [300, 500, 1000],      "nutrition": {"calories": 11, "salt": 0.002}},
    {"id": "v022", "name": "南瓜",  "category": "蔬菜", "emoji": "🎃",   "unit": "g",  "presets": [300, 500, 1000],      "nutrition": {"calories": 26, "salt": 0.001}},
    {"id": "v023", "name": "苦瓜",  "category": "蔬菜", "emoji": "🥝",   "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 19, "salt": 0.002}},
    {"id": "v024", "name": "莲藕",  "category": "蔬菜", "emoji": "🪷",   "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 74, "salt": 0.04}},
    {"id": "v025", "name": "蘑菇",  "category": "蔬菜", "emoji": "🍄",   "unit": "g",  "presets": [100, 200, 300],       "nutrition": {"calories": 22, "salt": 0.005}},
    {"id": "v026", "name": "木耳",  "category": "蔬菜", "emoji": "🪸",   "unit": "g",  "presets": [10, 30, 50],           "nutrition": {"calories": 25, "salt": 0.01}},
    {"id": "v027", "name": "西葫芦","category": "蔬菜", "emoji": "🥒",   "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 19, "salt": 0.002}},
    {"id": "v028", "name": "蒜苔",  "category": "蔬菜", "emoji": "🌿",   "unit": "g",  "presets": [100, 200, 300],       "nutrition": {"calories": 40, "salt": 0.003}},

    # ===== 肉蛋类 =====
    {"id": "m001", "name": "猪肉",   "category": "肉蛋", "emoji": "🐷", "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 395, "salt": 0.06}},
    {"id": "m002", "name": "猪里脊", "category": "肉蛋", "emoji": "🐷", "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 155, "salt": 0.05}},
    {"id": "m003", "name": "五花肉", "category": "肉蛋", "emoji": "🥓", "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 518, "salt": 0.04}},
    {"id": "m004", "name": "排骨",   "category": "肉蛋", "emoji": "🦴", "unit": "g",  "presets": [300, 500, 1000],      "nutrition": {"calories": 264, "salt": 0.08}},
    {"id": "m005", "name": "鸡胸肉", "category": "肉蛋", "emoji": "🐔", "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 133, "salt": 0.04}},
    {"id": "m006", "name": "鸡腿",   "category": "肉蛋", "emoji": "🍗", "unit": "g",  "presets": [300, 450, 600],       "weightNote": "约150g/个", "nutrition": {"calories": 181, "salt": 0.07}},
    {"id": "m007", "name": "鸡翅",   "category": "肉蛋", "emoji": "🍗", "unit": "g",  "presets": [200, 300, 500],       "weightNote": "约50g/个", "nutrition": {"calories": 194, "salt": 0.06}},
    {"id": "m008", "name": "鸡蛋",   "category": "肉蛋", "emoji": "🥚", "unit": "g",  "presets": [100, 200, 300, 500],  "weightNote": "约55g/个", "nutrition": {"calories": 144, "salt": 0.13}},
    {"id": "m009", "name": "牛肉",   "category": "肉蛋", "emoji": "🐮", "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 125, "salt": 0.05}},
    {"id": "m010", "name": "牛腩",   "category": "肉蛋", "emoji": "🐮", "unit": "g",  "presets": [300, 500, 1000],      "nutrition": {"calories": 180, "salt": 0.05}},
    {"id": "m011", "name": "虾仁",   "category": "肉蛋", "emoji": "🦐", "unit": "g",  "presets": [100, 200, 300],       "nutrition": {"calories": 99,  "salt": 0.2}},
    {"id": "m012", "name": "鱼",     "category": "肉蛋", "emoji": "🐟", "unit": "g",  "presets": [500, 1000],           "weightNote": "约500g/条", "nutrition": {"calories": 110, "salt": 0.06}},
    {"id": "m013", "name": "虾",     "category": "肉蛋", "emoji": "🦐", "unit": "g",  "presets": [200, 300, 500],       "nutrition": {"calories": 93,  "salt": 0.17}},
    {"id": "m014", "name": "蛤蜊",   "category": "肉蛋", "emoji": "🐚", "unit": "g",  "presets": [300, 500, 1000],      "nutrition": {"calories": 62,  "salt": 0.5}},
    {"id": "m015", "name": "火腿肠", "category": "肉蛋", "emoji": "🌭", "unit": "g",  "presets": [50, 100, 150],         "weightNote": "约50g/根", "nutrition": {"calories": 212, "salt": 2.0}},

    # ===== 豆制品 =====
    {"id": "d001", "name": "豆腐",   "category": "豆制品", "emoji": "🧈", "unit": "g",  "presets": [200, 300, 500], "nutrition": {"calories": 76,  "salt": 0.007}},
    {"id": "d002", "name": "老豆腐", "category": "豆制品", "emoji": "🧈", "unit": "g",  "presets": [200, 300, 500], "nutrition": {"calories": 82,  "salt": 0.007}},
    {"id": "d003", "name": "嫩豆腐", "category": "豆制品", "emoji": "🧈", "unit": "g",  "presets": [200, 300, 500], "nutrition": {"calories": 62,  "salt": 0.007}},
    {"id": "d004", "name": "豆皮",   "category": "豆制品", "emoji": "🟫", "unit": "g",  "presets": [100, 200, 300], "nutrition": {"calories": 159, "salt": 0.01}},
    {"id": "d005", "name": "豆干",   "category": "豆制品", "emoji": "🟫", "unit": "g",  "presets": [100, 200, 300], "nutrition": {"calories": 161, "salt": 0.02}},
    {"id": "d006", "name": "腐竹",   "category": "豆制品", "emoji": "🟫", "unit": "g",  "presets": [30, 50, 100],   "nutrition": {"calories": 155, "salt": 0.01}},
    {"id": "d007", "name": "皮蛋",   "category": "豆制品", "emoji": "🥚", "unit": "g",  "presets": [60, 120, 180],        "weightNote": "约60g/个", "nutrition": {"calories": 171, "salt": 0.8}},

    # ===== 主食类 =====
    {"id": "s001", "name": "大米",   "category": "主食", "emoji": "🍚",   "unit": "g",  "presets": [100, 200, 300],       "nutrition": {"calories": 346, "salt": 0.003}},
    {"id": "s002", "name": "面条",   "category": "主食", "emoji": "🍜",   "unit": "g",  "presets": [100, 200, 300],       "nutrition": {"calories": 284, "salt": 0.002}},
    {"id": "s003", "name": "面粉",   "category": "主食", "emoji": "🌾",   "unit": "g",  "presets": [200, 500, 1000],      "nutrition": {"calories": 364, "salt": 0.002}},
    {"id": "s004", "name": "馒头",   "category": "主食", "emoji": "🥟",   "unit": "g",  "presets": [100, 200, 300],       "weightNote": "约100g/个", "nutrition": {"calories": 223, "salt": 0.1}},
    {"id": "s005", "name": "粉丝",   "category": "主食", "emoji": "🍝",   "unit": "g",  "presets": [30, 50, 100],          "nutrition": {"calories": 338, "salt": 0.005}},
    {"id": "s006", "name": "面包",   "category": "主食", "emoji": "🍞",   "unit": "g",  "presets": [60, 120, 180],        "weightNote": "约30g/片", "nutrition": {"calories": 266, "salt": 0.5}},
]

# 默认分类排序（只显示用户需要选择的分类）
CATEGORY_ORDER = ["蔬菜", "肉蛋", "豆制品", "主食"]

# 默认拥有的食材（厨房常备，不需要用户选择，不计入缺食材）
# 包含：基础调料 + 葱姜蒜
BASIC_SEASONINGS = [
    "盐", "生抽", "老抽", "料酒", "醋", "白糖", "淀粉", "食用油", "蚝油",
    "葱", "生姜", "大蒜", "干辣椒", "花椒", "豆瓣酱",
]

# 需要过滤掉的"默认拥有"食材（不在选择列表中展示）
DEFAULT_NAMES = {"葱", "生姜", "大蒜"}

# 供前端使用的食材列表（已去除默认拥有的食材）
VISIBLE_INGREDIENTS = [i for i in INGREDIENTS if i.get("category") != "调味料" and i["name"] not in DEFAULT_NAMES]

# 所有标签（供探索Tab筛选使用）
ALL_TAGS = [
    "下饭", "快手菜", "一人食", "经典", "家常", "清淡", "辣", "健康",
    "川菜", "硬菜", "多人食", "素菜", "凉菜", "夏季", "主食", "汤",
    "新手友好", "宴客", "减脂", "无需开火", "营养均衡", "下火",
    "东北菜", "湖南菜", "港式", "上海", "北京菜",
]
