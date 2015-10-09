import moco.actuator
import moco.motion_ops.base


class Attachment:

    def __init__(self, actuator: moco.actuator.Actuator=None):
        self.actuator = actuator

        self.motion_ops = []
        self._active_motion_op = None

    def queue_motion_op(self, motion_op: moco.motion_ops.base.MotionOp):
        self.motion_ops.append(motion_op)
        if self.actuator:
            self.actuator.queue_motion_op(motion_op)

    def clear_active_motion_op(self):
        self._active_motion_op = None
        if self.actuator:
            self.actuator.clear_active_motion_op()

    @property
    def is_motion_op_complete(self):
        return True

    def on_tick(self):
        print('Attachment')
