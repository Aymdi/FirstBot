

class Autopilot:

    _speed_1 = 0
    _speed_2 = 0

    def __init__(self, speed_max, delta_max):
        self._speed_max = speed_max
        self._delta_max = delta_max

    def get_speed(self):
        return - self._speed_1, self._speed_2

    def init_speed(self):
        self._speed_1 = self._speed_max
        self._speed_2 = self._speed_max

        return self.get_speed()

    def compute_speed(self, delta):
        speed = 0
        # r = 0
        # if delta // self._delta_max == 0 :
        #     r = delta % self._delta_max
        #     speed = self._speed_max * r

        self._speed_1, self._speed_2 = speed, speed

        if delta > 0 :
            self._speed_2 += self._speed_max
        else :
            self._speed_1 += self._speed_max

        return self.get_speed()
