import time


class TrafficLight:
    _color = None
    _colors = ['red', 'yellow', 'green']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        color = 0
        while color < 5:
            for el in TrafficLight._colors:
                print(el)
                color += 1
                time.sleep(1)


traffic = TrafficLight()
traffic.running()
