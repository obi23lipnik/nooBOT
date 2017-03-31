import win32api, win32con
from time import sleep
from random import randint

class Action(object):
    # Init will require input of absolute coordinates (by pixle) for each angle point
    ## If no values are specified, the surface is set to 800x600 and with minimum coordinate of (0, 0) -
    def __init__(self, x_minimum=0, y_minimum=0, x_maximum=800, y_maximum=600):
        self.x_minimum = x_minimum
        self.y_minimum = y_minimum
        self.x_maximum = x_maximum
        self.y_maximum = y_maximum

    def get_pos(self):
        return win32api.GetCursorPos()

    def set_pos(self, x, y, verbose=False):
        x, y = self.x_minimum + x, self.y_minimum + y

        if x > self.x_maximum:
            x = self.x_maximum

        if y > self.y_maximum:
            y = self.y_maximum

        win32api.SetCursorPos((x, y))

        if verbose:
            return 'Moved to ({0}, {1})'.format(x, y)

    def pseudo_human_move(self, xm=0, ym=0):
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
            x, y = self.get_pos()
            if reverse_ym:
                self.set_pos(x, y-1)
            else:
                self.set_pos(x, y+1)

        for _ in range(xm):
            sleep(0.001)
            x, y = self.get_pos()
            if reverse_xm:
                self.set_pos(x-1, y)
            else:
                self.set_pos(x+1, y)

    def human_sleep(self, ):
        sleep(float('{sec}.{msec}'.format(sec=randint(0, 1), msec=randint(100,999))))

    def wait(self, sec, dsec, msec):
        sleep(float('{sec}.{dsec}{msec}'.format(sec=sec, dsec=dsec, msec=msec)))

    def right_click(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()
        self.set_pos(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

    def right_hold(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()

        self.set_pos(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)

    def right_release(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()

        self.set_pos(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

    def left_click(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()
        self.set_pos(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    def left_hold(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()

        self.set_pos(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)

    def left_release(self, x=None, y=None):
        if not x or not y:
            x, y = self.get_pos()

        self.set_pos(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

