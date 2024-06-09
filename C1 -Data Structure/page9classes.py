import math
class _Circle:
    def __init__(self, r):
        self._r = r
    def _calarea(self):
        self._area = math.pi * math.pow(self._r, 2)

class Area:
    area =0
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area_cal(self):
        self.area = self.length * self.breadth
        return 0

