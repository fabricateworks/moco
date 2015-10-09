import time


class RateLimiter:

    def __init__(self, hertz=60):
        self.hertz = float(hertz)
        self._last_cycle_time = None

    def _tick(self):
        current_time = time.time()
        delta = current_time - self._last_cycle_time
        if delta >= 1.0 / self.hertz:
            self._last_cycle_time = current_time
            self.tick()

    def tick(self):
        pass

    def start(self):
        self._last_cycle_time = time.time()
        while True:
            self._tick()
