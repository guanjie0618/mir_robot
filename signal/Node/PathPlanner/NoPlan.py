from itertools import compress


def plan(points: tuple):
    points_x, points_y, points_in = points

    points_x = points_x.flatten()
    points_y = points_y.flatten()
    points_in = points_in.flatten()

    points_x = list(compress(points_x, points_in))
    points_y = list(compress(points_y, points_in))

    return points_x, points_y
