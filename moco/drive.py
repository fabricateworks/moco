import moco.motion_ops.base


class Drive:

    def __init__(self):
        self.motion_ops = []
        self._active_motion_op = None

    def queue_motion_op(self, motion_op: moco.motion_ops.base.MotionOp):
        self.motion_ops.append(motion_op)

    def clear_active_motion_op(self):
        self._active_motion_op = None

    def tick(self):
        pass
