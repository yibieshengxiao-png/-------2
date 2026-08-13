# -*- coding: utf-8 -*-
"""批量生成图标：从需求表解析 -> 调千问 API -> 按命名规范保存"""
import re, os, sys, io, json, time, urllib.request, urllib.parse, threading

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

STYLE = "二次元插画风格，日系美食插画，细线描边，平涂上色，明亮清新配色，45度俯视，单一主体居中，透明背景，无文字"
API_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"
KEY = "sk-ws-H.EEILPMD.tGYL.MEQCIEj0WkS-h38t6PRus_Vksc8SLzWJyUJN2dpahlFP0BgsAiBdHnUIuosrM9RVOMw0Yzo3aRPH9CuGpaarbqR8gZX8tw"
OUT_DIR = r"D:\冠之今天吃什么\icons"
REQ_MD = r"D:\冠之今天吃什么\图标需求表.md"

def parse_items():
    """解析需求表，返回 [(id, name, desc, type)] type: ing/recipe"""
    with open(REQ_MD, encoding='utf-8') as f:
        content = f.read()
    items = []
    # 食材表: 2.1~2.4 节，行格式 | v001 | 青椒 | 描述... |
    # 食谱表: 3.1~3.11 节
    lines = content.split('\n')
    in_ing = False
    in_recipe = False
    for line in lines:
        if re.match(r'^### 2\.', line.strip()):
            in_ing, in_recipe = True, False
            continue
        if re.match(r'^### 3\.', line.strip()):
            in_ing, in_recipe = False, True
            continue
        if re.match(r'^## ', line.strip()):
            in_ing, in_recipe = False, False
            continue
        m = re.match(r'^\|\s*([a-z]\d{3})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', line.strip())
        if not m:
            continue
        iid, name, desc = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        if in_ing:
            items.append((iid, name, desc, 'ing'))
        elif in_recipe:
            items.append((iid, name, desc, 'recipe'))
    return items

def gen_one(iid, name, desc, kind):
    """生成一张图，失败自动重试（最多 3 次），返回 True/False"""
    prompt = f"{desc}。{STYLE}"
    body = json.dumps({
        "model": "qwen-image-3.0-pro",
        "input": {"messages": [{"role": "user", "content": [{"text": prompt}]}]},
        "parameters": {"size": "1024*1024", "n": 1, "watermark": False, "prompt_extend": False}
    }, ensure_ascii=False).encode('utf-8')
    for attempt in range(4):
        try:
            req = urllib.request.Request(API_URL, data=body, headers={
                "Authorization": f"Bearer {KEY}",
                "Content-Type": "application/json"
            })
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode('utf-8'))
            img_url = data['output']['choices'][0]['message']['content'][0]['image']
            fname = f"{'ing' if kind=='ing' else 'recipe'}_{iid}.png"
            fpath = os.path.join(OUT_DIR, fname)
            urllib.request.urlretrieve(img_url, fpath)
            return fname
        except Exception as e:
            if attempt < 3:
                wait = 5 * (attempt + 1)
                time.sleep(wait)
            else:
                raise

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    items = parse_items()
    ing = [x for x in items if x[3] == 'ing']
    recipe = [x for x in items if x[3] == 'recipe']
    print(f"解析到: 食材 {len(ing)} 个, 食谱 {len(recipe)} 个, 共 {len(items)} 个")
    # 检查已存在的
    done = set(os.listdir(OUT_DIR))
    todo = [x for x in items if f"{'ing' if x[3]=='ing' else 'recipe'}_{x[0]}.png" not in done]
    print(f"待生成: {len(todo)} 个 (已有 {len(items)-len(todo)} 个)")
    
    lock = threading.Lock()
    ok, fail = [], []
    def worker():
        while True:
            with lock:
                if not todo: return
                item = todo.pop(0)
            iid, name, desc, kind = item
            try:
                fname = gen_one(iid, name, desc, kind)
                with lock:
                    ok.append(fname)
                    print(f"[OK] {fname} ({name}) 剩余{len(todo)}", flush=True)
            except Exception as e:
                with lock:
                    fail.append((iid, name, str(e)[:100]))
                    print(f"[FAIL] {iid} {name}: {str(e)[:80]}", flush=True)
            time.sleep(1)
    
    threads = [threading.Thread(target=worker) for _ in range(1)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"\n完成: 成功 {len(ok)}, 失败 {len(fail)}")
    for f in fail[:10]:
        print(f"  FAILED: {f[0]} {f[1]}: {f[2]}")
    # 写失败清单
    if fail:
        with open(os.path.join(OUT_DIR, "_failed.txt"), 'w', encoding='utf-8') as f:
            for iid, name, err in fail:
                f.write(f"{iid}\t{name}\t{err}\n")

if __name__ == '__main__':
    main()
