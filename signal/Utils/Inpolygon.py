import numpy as np
from matplotlib.path import Path
from numpy import vstack, hstack


# Matlab原始版 inpolygon函數
def inpolygon_Matlab(x_point, y_point, x_area, y_area):
    """
    Reimplement inpolygon in matlab
    :type x_point: np.ndarray
    :type y_point: np.ndarray
    :type x_area: np.ndarray
    :type y_area: np.ndarray
    """
    # 合併xv和yv為頂點數組
    vertices = vstack((x_area, y_area)).T
    # 定義Path對象
    path = Path(vertices)
    # 把xq和yq合併為test_points
    test_points = hstack([x_point.reshape(x_point.size, -1), y_point.reshape(y_point.size, -1)])
    # 得到一個test_points是否嚴格在path內的mask，是bool值數組
    _in = path.contains_points(test_points)
    # 得到一個test_points是否在path內部或者在路徑上的mask
    _in_on = path.contains_points(test_points, radius=-1e-10)
    # 得到一個test_points是否在path路徑上的mask
    _on = _in ^ _in_on
    return _in_on, _on


# 簡化inpolygon函數
def inpolygon(xq, yq, xv, yv):
    """
    reimplement inpolygon in matlab
    :type xq: np.ndarray
    :type yq: np.ndarray
    :type xv: np.ndarray
    :type yv: np.ndarray
    """
    # 合併xv和yv為頂點數組
    vertices = np.vstack((xv, yv)).T
    # 定義Path對象
    path = Path(vertices)
    # 把xq和yq合併為test_points
    test_points = np.hstack([xq.reshape(xq.size, -1), yq.reshape(yq.size, -1)])
    # 得到一個test_points是否嚴格在path內的mask，是bool值數組
    _in = path.contains_points(test_points)
    # 得到一個test_points是否在path內部或者在路徑上的mask
    _in_on = path.contains_points(test_points, radius=-1e-10)

    return _in_on


if __name__ == '__main__':
    # inpolygon 函數用法
    xv = np.array([-4, 0, 4, 0])
    yv = np.array([0, 4, 0, -4])
    X = np.array([0, 1, 3.5, 4, 5])
    Y = np.array([0, 1, 0, 0, 0])

    _in, _on = inpolygon_Matlab(X, Y, xv, yv)

    print(_in)
    print(_on)
