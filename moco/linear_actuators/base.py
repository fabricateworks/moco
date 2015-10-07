import weakref


class LinearActuator:

    def __init__(self):
        self._motor = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = weakref.proxy(motor)

    def rotate(self, amount):
        pass

