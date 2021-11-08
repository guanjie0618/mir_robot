from numpy import int64, round, sqrt


# 4捨5入
def round_int64(point):
    return int64(round(point))


# 計算與歸一點距離
def error_distance(y, x):
    nc_y, nc_x = round_int64((y, x))
    return sqrt((nc_y - y) ** 2 + (nc_x - x) ** 2)


if __name__ == '__main__':
    print(error_distance(3.6, 4.3))
    print(error_distance(3, 4))
    print(error_distance(3.5, 4))
