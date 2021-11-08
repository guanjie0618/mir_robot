from numpy import array, ones

from Utils.Statistical import min_error
from Utils.Error import error_distance as ed
from Utils.Error import round_int64 as rd


def map2darray(y: list, x: list, data: list, gap: float = 0.5, error_function=min_error):
    # convert to ndarray
    y = array(y)
    x = array(x)

    # scale
    y_scale = y / gap
    x_scale = x / gap

    # round
    y_norm = rd(y_scale)
    x_norm = rd(x_scale)

    # natural
    y_N = y_norm - y_norm.min()
    x_N = x_norm - x_norm.min()

    # data struct
    data_set = {p: {} for p in set(zip(y_norm, x_norm))}
    for yy, xx, dd in zip(y_scale, x_scale, data):
        data_set[(rd(yy), rd(xx))][ed(yy, xx)] = dd

    # create 2d minimum power map
    sizeY = y_N.max() - y_N.min() + 1
    sizeX = x_N.max() - x_N.min() + 1
    map2d = -120 * ones((sizeY, sizeX))

    for (yy, xx), dd in data_set.items():
        map2d[yy - y_norm.min()][xx - x_norm.min()] = error_function(dd)
    return map2d
