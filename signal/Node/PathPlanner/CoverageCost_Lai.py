# 取得(x, y)周圍8個點的座標
# 這裡注意，range 末尾是開區間，所以要加 1
def _get_around(x, y, psin):
    return [(i, j) for i in range(max(0, x - 1), min(psin.shape[1] - 1, x + 1) + 1)
            for j in range(max(0, y - 1), min(psin.shape[0] - 1, y + 1) + 1) if i != x or j != y]


# 取得目前所在座標點的周圍true點(周圍4點中，找到也是true的點)
def _get_around_true4(x1, y1, true_list, psin):
    a = [x for x in true_list if x in _get_between_xy(x1, y1, psin)]
    return a


# 取得x方向左右兩個座標
def _get_between_x(x, y, psin):
    return [(i, y) for i in range(max(0, x - 1), min(psin.shape[1] - 1, x + 1) + 1) if i != x]


# 取得y方向上下兩個座標
def _get_between_y(x, y, psin):
    return [(x, j) for j in range(max(0, y - 1), min(psin.shape[0] - 1, y + 1) + 1) if j != y]


# 取得座標(x,y)上下左右四個座標
def _get_between_xy(x, y, psin):
    return _get_between_x(x, y, psin) + _get_between_y(x, y, psin)


# 每個true點的cost
def _Path_cost(psin):
    Dict = {}
    true_list = []
    for y in range(psin.shape[0]):
        for x in range(psin.shape[1]):
            if psin[y][x] == True:
                true_list.append((x, y))
                a = _get_around(x, y, psin)
                count = 0
                for xx, yy in a:
                    if psin[yy][xx] == False:
                        count += 1
                Dict[(x, y)] = count
    return Dict


# 從true_list的第一個座標為起始點，取得其周圍的true點
def _next_step(x, y, true_list, pc, psin):
    List = []
    a = _get_around_true4(x, y, true_list, psin)
    for xx, yy in a:
        pc[(xx, yy)] += 1  # 將周圍的true點的cost +1
        d = pc[(xx, yy)]
        List.append(d)

    if List:
        Max_List = List.index(max(List))
        true_list.remove((x, y))
        return a[Max_List]
    else:
        try:
            true_list.remove((x, y))
            return true_list[0]
        except IndexError:
            pass


# 所有true點的index
def _true_list(psin):
    True_List = []
    for y in range(psin.shape[0]):
        for x in range(psin.shape[1]):
            if psin[y][x] == True:
                True_List.append((x, y))
    return True_List


def plan(points: tuple):
    points_x, points_y, points_in = points
    # 所有點要走的順序
    True_List = _true_list(points_in)
    path = []
    path.append(True_List[0])
    pc = _Path_cost(points_in)

    a = _next_step(True_List[0][0], True_List[0][1], True_List, pc, points_in)
    path.append(a)

    while True_List:
        # for _ in range (len(true_list)):
        b = _next_step(a[0], a[1], True_List, pc, points_in)
        if b != None:
            path.append(b)
            a = b

    point_x, point_y = [], []
    for px, py in path:
        point_x.append(points_x[py][px])
        point_y.append(points_y[py][px])

    return point_x, point_y
