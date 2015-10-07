import time


class RateLimiter:

    def __init__(self, hertz=60):
        self.hertz = float(hertz)
        self._last_cycle_time = None

    def tick(self):
        current_time = time.time()
        delta = current_time - self._last_cycle_time
        if delta >= 1.0 / self.hertz:
            self._last_cycle_time = current_time
            self.on_cycle()

    def start(self):
        self._last_cycle_time = time.time()
        while True:
            self.tick()

    def on_cycle(self):
        pass
