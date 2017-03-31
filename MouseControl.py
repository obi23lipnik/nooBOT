import win32api, win32con
from time import sleep
from random import randint


def get_pos():
    return win32api.GetCursorPos()

def set_pos(x, y):
    win32api.SetCursorPos((x,y))

def relative_move(xm=0, ym=0):
    reverse_xm, reverse_ym = False, False
    xm, ym = int(xm), int(ym)

    if xm < 0:
        reverse_xm = True
        xm *= -1

    if ym < 0:
        reverse_ym = True
        ym *= -1

    for _ in range(ym):
        sleep(0.001)
        x, y = get_pos()
        if reverse_ym:
            set_pos(x, y-1)
        else:
            set_pos(x, y+1)

    for _ in range(xm):
        sleep(0.001)
        x, y = get_pos()
        if reverse_xm:
            set_pos(x-1, y)
        else:
            set_pos(x+1, y)

def human_sleep():
    sleep(float('{sec}.{msec}'.format(sec=randint(0, 1), msec=randint(100,999))))

def wait(sec, dsec, msec):
    sleep(float('{sec}.{dsec}{msec}'.format(sec=sec, dsec=dsec, msec=msec)))


def right_click(x=None, y=None):
    if not x or not y:
        x, y = get_pos()
    set_pos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

def right_hold(x=None, y=None):
    if not x or not y:
        x, y = get_pos()

    set_pos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)

def right_release(x=None, y=None):
    if not x or not y:
        x, y = get_pos()

    set_pos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

def left_click(x=None, y=None):
    if not x or not y:
        x, y = get_pos()
    set_pos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def left_hold(x=None, y=None):
    if not x or not y:
        x, y = get_pos()

    set_pos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)

def left_release(x=None, y=None):
    if not x or not y:
        x, y = get_pos()

    set_pos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)