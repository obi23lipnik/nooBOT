from MouseControl import Action as Mouse_Action
import time

class Record(object):
    def __init__(self, x_minimum=62, y_minimum=0, x_maximum=862, y_maximum=600):
        self.last_pos = (0,0)
        self.start_time = time.time()
        self.mouse = Mouse_Action(x_minimum, y_minimum, x_maximum, y_maximum)

    def position_tracking(self):
        if not self.last_pos == self.mouse.get_pos():
            last_pos = self.mouse.get_pos()
            return last_pos, round((time.time() - self.start_time),2)
        self.mouse.wait(0,0,5)