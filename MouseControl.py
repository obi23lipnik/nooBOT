from time import sleep
from random import randint

import win32api, win32con


class Action(object):
    # Init will require input of absolute coordinates (by pixel) for each angle point
    ## If no values are specified, the surface is set to 800x600 and with minimum coordinate of (0, 0)
    def __init__(self, x_minimum=0, y_minimum=0, x_maximum=800, y_maximum=600):
        self.x_lowest = x_minimum
        self.y_lowest = y_minimum
        self.x_maximum = x_maximum
        self.y_maximum = y_maximum

    @staticmethod
    def is_reversed(value):
        return value < 0

    @staticmethod
    def get_pos():
        return win32api.GetCursorPos()

    def set_pos(self, x, y, verbose=False):
        if x > self.x_maximum:
            x = self.x_maximum
        elif x < self.x_lowest:
            x = self.x_lowest

        if y > self.y_maximum:
            y = self.y_maximum
        elif y < self.y_lowest:
            y = self.y_lowest

        win32api.SetCursorPos((x, y))

        if verbose:
            print 'Moved to ({0}, {1})'.format(x, y)

    @staticmethod
    def bow_binary_range(x_len, y_len):
        if x_len >= y_len:
            division = x_len / y_len
            point = x_len % y_len
            if point == 0:
                dir_range = [True for direction in range(x_len)]
                i = 0
                for direction in dir_range:
                    if




    def pseudo_human_move(self, move_right=0, move_down=0, verbose=False):
        reverse_xm, reverse_ym = self.is_reversed(move_right), self.is_reversed(move_down)
        move_right, move_down = int(move_right), int(move_down)

        for _ in range(abs(move_down)):
            sleep(0.001)
            x, y = self.get_pos()
            if reverse_ym:
                self.set_pos(x, y - 1, verbose)
            else:
                self.set_pos(x, y + 1, verbose)

    def pseudo_human_sleep(self, ):
        sleep(float('{sec}.{msec}'.format(sec=randint(0, 1), msec=randint(100, 999))))

    def wait(self, sec=0, dsec=0, msec=0):
        sleep(float('{sec}.{dsec}{msec}'.format(sec=sec, dsec=dsec, msec=msec)))

    def right_click(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()
        self.set_pos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

    def right_hold(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()

        self.set_pos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)

    def right_release(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()

        self.set_pos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

    def left_click(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()
        self.set_pos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def left_hold(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()

        self.set_pos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)

    def left_release(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()

        self.set_pos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
