import moco.config
import moco.sensors.rotary_encoder
import moco.motors.base


class Servo(moco.motors.base.Motor):

    def __init__(self, rotary_encoder=None):
        self.rotary_encoder = None
        if not rotary_encoder:
            self.rotary_encoder = moco.sensors.rotary_encoder.RotaryEncoder()

        self.perfect_rotation = 0.0

        # Positive is clockwise
        self._speed = 0.0
        self._rotates = None

    @property
    def speed(self):
        return self._speed

    def set_speed(self, rpm):
        self._speed = rpm

    @property
    def rotates(self):
        return self._rotates

    @rotates.setter
    def rotates(self, rotates):
        rotates.motor = self
        self._rotates = rotates

    def tick(self):
        speed = self.speed / (moco.config.HERTZ * 60)
        # self.rotates.rotate(self.speed)
        self.perfect_rotation += speed
        self.rotary_encoder.rotation += speed
