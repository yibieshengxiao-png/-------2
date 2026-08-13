# -*- coding: utf-8 -*-
# 批量去除图标近白背景（flood fill 从边缘抠透明），并重新压缩保存
import os, sys
import numpy as np
from PIL import Image
from collections import deque
from scipy import ndimage

sys.stdout.reconfigure(encoding='utf-8')

ICON_DIR = 'icons'
TOLERANCE = 26  # 与背景色的欧氏距离阈值


def remove_bg(arr):
    h, w = arr.shape[:2]
    rgb = arr[:, :, :3].astype(np.int32)
    alpha = arr[:, :, 3].copy()

    corners = [(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)]
    ref = np.mean([rgb[y, x] for x, y in corners], axis=0)

    diff = rgb - ref
    dist = np.sqrt((diff * diff).sum(axis=2))
    bg = dist < TOLERANCE

    visited = np.zeros((h, w), dtype=bool)
    dq = deque()
    for x in range(w):
        for y in (0, h - 1):
            if bg[y, x]:
                visited[y, x] = True
                dq.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if bg[y, x] and not visited[y, x]:
                visited[y, x] = True
                dq.append((y, x))

    while dq:
        y, x = dq.popleft()
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < h and 0 <= nx < w and bg[ny, nx] and not visited[ny, nx]:
                visited[ny, nx] = True
                dq.append((ny, nx))

    alpha[visited] = 0

    # 边缘羽化：菜品最外圈 1px 半透明，柔化锯齿/白边
    opaque = alpha > 0
    eroded = ndimage.binary_erosion(opaque, iterations=1)
    boundary = opaque & ~eroded
    alpha[boundary] = (alpha[boundary] * 0.5).astype(np.uint8)

    out = arr.copy()
    out[:, :, 3] = alpha
    return out


def process(path):
    im = Image.open(path).convert('RGBA')
    arr = np.array(im)
    return Image.fromarray(remove_bg(arr))


if __name__ == '__main__':
    files = sorted(f for f in os.listdir(ICON_DIR) if f.endswith('.png'))
    print(f'共 {len(files)} 张图标，开始批量抠透明...')
    done = 0
    for f in files:
        p = os.path.join(ICON_DIR, f)
        before = os.path.getsize(p)
        process(p).save(p, optimize=True)
        after = os.path.getsize(p)
        done += 1
    print(f'完成 {done} 张。')
