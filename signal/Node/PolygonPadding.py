from itertools import cycle, islice

import numpy as np

from Utils.Inpolygon import inpolygon
from Utils.Vector import vector


# 將可走範圍內縮
def padding(area: tuple, size: float):
    x, y = area

    # it = [1, 2, 3, ..., n, 0]  # cycle[1:1-len]
    x_pre = islice(cycle(x), 1, 1 + len(x))
    y_pre = islice(cycle(y), 1, 1 + len(y))
    # it = [n, 0, 1, 2, ..., n-1]  # cycle[len-1:2*len-1]
    x_next = islice(cycle(x), len(x) - 1, 2 * len(x) - 1)
    y_next = islice(cycle(y), len(y) - 1, 2 * len(x) - 1)

    px = []
    py = []

    # 確認p點是否在邊緣內或邊緣上
    def in_polygon(p): return inpolygon(p[0], p[1], x, y)

    for xp, yp, xx, yy, xn, yn in zip(x_pre, y_pre, x, y, x_next, y_next):
        point = np.array([xx, yy])
        # 計算向量
        v1 = vector.from_point(xp, yp, xx, yy)
        v2 = vector.from_point(xx, yy, xn, yn)
        # 單位向量相加
        meta = v1.unit_vector() + v2.unit_vector()

        if in_polygon(point + size * meta.normal_vector_x().unit_vector().v):
            angular_bisector = meta.normal_vector_x().unit_vector()
        else:
            angular_bisector = meta.normal_vector_y().unit_vector()

        # 角平分線 * sin = size
        pad = size / vector.sin(v1, angular_bisector)
        pad_point = point + pad * angular_bisector.v
        px.append(pad_point[0])
        py.append(pad_point[1])

    # 又回到最初的起點，呆呆地站在鏡子前
    px.append(px[0])
    py.append(py[0])

    return px, py
