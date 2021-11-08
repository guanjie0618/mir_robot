import math

import numpy as np


# 計算兩點向量與向量[1, 0]夾角
def angle(x1, y1, x2, y2):
    v = np.array([x2 - x1, y2 - y1])
    uv = np.array([1, 0])

    L = np.sqrt(v @ v)
    cos_angle = v[0] / L
    radian = np.arccos(cos_angle)
    angle_ = radian * 360 / 2 / np.pi * np.sign(np.cross(uv, v))
    return angle_


# 同上，用vector物件重寫
def angle_vector(x1, y1, x2, y2):
    v = vector.from_point(x1, y1, x2, y2)
    uv = vector(1, 0)
    return uv.angle_with(v)


# 同上，計算速度最快
def angle_Performance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    uv = [1, 0]
    cos_angle = dx / math.sqrt(dx ** 2 + dy ** 2)
    angle_ = np.arccos(cos_angle) * 360 / 2 / np.pi * np.sign(np.cross(uv, [dx, dy]))
    return angle_


# 向量實用物件
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = np.array([x, y])
        self.L = self.length()

    # 建立物件,input兩個點
    @staticmethod
    def from_point(x_t, y_t, x_t1, y_t2):
        return vector(x_t1 - x_t, y_t2 - y_t)

    # 建立物件,input一個二維numpy.ndarray
    @staticmethod
    def from_ndarray(v: 'np.ndarray'):
        if v.shape == (2,):
            return vector(v[0], v[1])
        else:
            return None

    # 建立物件,input一個二維list
    @staticmethod
    def from_list(v: list):
        if len(v) == 2:
            return vector(v[0], v[1])
        else:
            return None

    # 向量長度
    def length(self):
        return np.sqrt(np.sum(self.v ** 2))

    # 單位向量
    def unit_vector(self):
        dx, dy = self.v / self.L
        return vector(dx, dy)

    # 法向量1
    def normal_vector_x(self):
        return vector(-self.y, self.x)

    # 法向量2
    def normal_vector_y(self):
        return vector(self.y, -self.x)

    # 跟另一個向量的cos
    def cos_with(self, vec2: 'vector'):
        return np.inner(self.v, vec2.v) / (self.L * vec2.L)

    # 跟另一個向量的sin
    def sin_with(self, vec2: 'vector'):
        cos = self.cos_with(vec2)
        return np.sqrt(1 - cos ** 2)

    # 跟另一個向量的弧度
    def radian_with(self, vec2: 'vector'):
        cos = self.cos_with(vec2)
        return np.arccos(cos)

    # 跟另一個向量的角度
    def angle_with(self, vec2: 'vector'):
        radian = self.radian_with(vec2)
        angle_ = radian * 360 / 2 / np.pi * np.sign(np.cross(self.v, vec2.v))
        return angle_

    def __str__(self):
        return f'({self.x}, {self.y})'

    # 可以直接將兩個向量相加運算
    def __add__(self, other: 'vector'):
        return vector(self.x + other.x, self.y + other.y)

    # 計算兩個向量cos
    @staticmethod
    def cos(vec1: 'vector', vec2: 'vector'):
        return np.inner(vec1.v, vec2.v) / (vec1.L * vec2.L)

    # 計算兩個向量sin
    @staticmethod
    def sin(vec1: 'vector', vec2: 'vector'):
        return np.sqrt(1 - vector.cos(vec1, vec2) ** 2)

    # 計算兩個向量弧度
    @staticmethod
    def radian(vec1: 'vector', vec2: 'vector'):
        cos = vector.cos(vec1, vec2)
        return np.arccos(cos)

    # 計算兩個向量角度
    @staticmethod
    def angle(vec1: 'vector', vec2: 'vector'):
        radian = vector.radian(vec1, vec2)
        angle_ = radian * 360 / 2 / np.pi * np.sign(np.cross(vec1.v, vec2.v))
        return angle_

    __repr__ = __str__


if __name__ == '__main__':
    """
    vector物件用法
    """
    import matplotlib.pyplot as plt
    x = [0, 1, 1]
    y = [0, 0, 1]

    v1 = vector.from_point(x[0], y[0], x[1], y[1])
    v2 = vector.from_point(x[1], y[1], x[2], y[2])
    meta = v1 + v2
    angular_bisector = meta.normal_vector_x().unit_vector()
    point = np.array([x[1], y[1]])
    pad = 0.45 / vector.sin(v1, angular_bisector)
    pad_point = point + pad * angular_bisector.v
    plt.plot(x, y)
    plt.plot(pad_point[0], pad_point[1], '*')
    plt.show()
    print(pad_point)
