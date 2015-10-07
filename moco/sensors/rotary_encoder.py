class RotaryEncoder:

    def __init__(self):
        self._rotation = 0

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value
