import moco.motion_ops.base


class LinearDistance(moco.motion_ops.base.MotionOp):

    def __init__(self, distance=0, speed=100):
        self.distance = distance
        # Units per minute
        self.speed = speed

        # Time here is represented in milliseconds
        self.acceleration_time = 500
        self.deceleration_time = 500

        self._started_at = {}
        self._wait_for = {}
        self._normalized_direction_vector = 0
