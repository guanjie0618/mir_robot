import os

from pyautogui import Point


def GET_joy_position() -> 'Point':
    PcName = os.getenv("COMPUTERNAME")  # Windows
    if PcName == 'DESKTOP-5N065OE':
        return Point(x=3432, y=393)
    elif PcName == 'vivobook':
        return Point(x=1432, y=666)


if __name__ == '__main__':
    print(os.getenv("COMPUTERNAME"))
