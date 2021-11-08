"""
Axises:
0 - x axis right stick  (+1 is right, -1 is left)
1 - y axis right stick  (+1 is down, -1 is up)
2 - trigger             (+1 is right, -1 is up)
3 - y axis left stick   (+1 is down, -1 is up)
4 - x axis left stick   (+1 is right, -1 is left)
"""
config = {
    'button': {
        0: (0, 100),  # A
        1: (100, 0),  # B
        2: (-100, 0),  # X
        3: (0, -100),  # Y
        4: (-50, 0),  # L1
        5: (50, 0),  # R1
    },
    'select': 6,
    'exit': 7,
    'axis': {
        0: (100, 0),
        # 1: (0, 100),
        2: (0, 50),
        # 3: (0, 50),
        4: (50, 0)
    },
    'hat': {
        0: (50, -50),
    }
}
