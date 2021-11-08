from numpy import save as npy
from pandas import DataFrame


# 儲存csv檔
def csv(path, array):
    """
    :param path: save path
    :param array: param
    :return: None
    """
    DataFrame(array).to_csv(path, index=False)


# 儲存地圖二維陣列
def map(path, map2d):
    """
    Save Data of map
    :param path: save path
    :param map2d: map data
    :return: None
    """
    # Storage csv data
    csv(path + 'map.csv', map2d)
    # Storage numpy data(.npy)
    npy(path + 'map', map2d)


# 儲存抓到的原始資料
def map_original_data(path, y, x, data):
    """
    Save original data of y, x, data
    :param path: save path
    :param y: list of y
    :param x: list of x
    :param data: list of data
    :return: None
    """
    npy(path + 'y', y)
    npy(path + 'x', x)
    npy(path + 'data', data)
