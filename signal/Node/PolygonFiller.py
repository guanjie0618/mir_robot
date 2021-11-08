import numpy as np

from Utils.Inpolygon import inpolygon


# 建立可走點，要用inpolygon篩掉不能走的點
def fill(area, gap):
    bot_x, bot_y = area
    points_y, points_x = np.mgrid[min(bot_y):max(bot_y):gap, min(bot_x):max(bot_x):gap]
    points_in = inpolygon(points_x, points_y, np.array(bot_x), np.array(bot_y)).reshape(points_x.shape)

    return points_x, points_y, points_in
