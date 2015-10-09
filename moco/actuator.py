import moco.drive
import moco.motion_ops.base


class Actuator:

    def __init__(self, drive: moco.drive.Drive=None):
        self.drive = drive

        self.motion_ops = []
        self._active_motion_op = None

    def queue_motion_op(self, motion_op: moco.motion_ops.base.MotionOp):
        self.motion_ops.append(motion_op)
        if self.drive:
            self.drive.queue_motion_op(motion_op)

    def clear_active_motion_op(self):
        self._active_motion_op = None
        if self.drive:
            self.drive.clear_active_motion_op()

    def tick(self):
        pass
