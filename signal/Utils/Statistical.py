"""
歸一點處理Function
"""
from numpy import array, average, sqrt, pi, exp


def _getKeyValue(data: dict):
    values = array(list(data.values()))
    keys = array(list(data.keys()))
    return keys, values



def _gaussian(x, sigma):
    return 1 / (sigma * sqrt(2 * pi)) * exp(-x ** 2 / (2 * sigma ** 2))



def _linear(x):
    return 1 - 2 * x


# power最小值
def value_min(data: dict):
    keys, values = _getKeyValue(data)
    return min(values)


# power最大值
def value_max(data: dict):
    keys, values = _getKeyValue(data)
    return max(values)


# 離歸一點最近點
def min_error(data: dict):
    keys, values = _getKeyValue(data)
    return data[min(keys)]


# power平均值
def avg_normal(data: dict):
    keys, values = _getKeyValue(data)
    return average(values)


# 高斯加權
class avg_gaussian:
    def __init__(self, sigma):
        self.sigma = sigma

    def function(self, data: dict):
        keys, values = _getKeyValue(data)
        return average(values, weights=_gaussian(keys * 10, sigma=self.sigma))


# 線性平均
def avg_linear(data: dict):
    keys, values = _getKeyValue(data)
    return average(values, weights=_linear(keys))


if __name__ == '__main__':
    d = {0.2: -10,
         0.1: -20,
         0.3: -30}
    # print(value_max(d))
    # print(value_min(d))
    # print(min_error(d))
    # print(avg_normal(d))
    print(avg_gaussian(d))
    print(avg_linear(d))
