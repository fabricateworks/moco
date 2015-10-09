import moco.motion_ops.base


class MotionHandler:

    CHILD_PROPERTY = 'child'

    def __init__(self):
        self.motion_ops = []
        self._active_motion_op = None

    def queue_motion_op(self, motion_op: moco.motion_ops.base.MotionOp):
        self.motion_ops.append(motion_op)

    def disperse_motion_op(self, motion_op: moco.motion_ops.base.MotionOp):
        """
        Propagate motion operations down to children.  Generally this means
        meaningful breakdown of a higher-level operation into a lower-level
        one.
        """
        if self.__dict__[self.CHILD_PROPERTY]:
            self.__dict__[self.CHILD_PROPERTY].queue_motion_op(motion_op)

    @property
    def is_motion_op_complete(self):
        """
        If we have an active motion operation, we should check the child to
        see if it is done.  Otherwise, let's assume we're done.
        """
        if self._active_motion_op:
            if self.__dict__[self.CHILD_PROPERTY]:
                return self.__dict__[self.CHILD_PROPERTY].is_motion_op_complete
            else:
                return True
        else:
            return True

    def clear_active_motion_op(self):
        self._active_motion_op = None
        if self.__dict__[self.CHILD_PROPERTY]:
            self.__dict__[self.CHILD_PROPERTY].clear_active_motion_op()

    def tick(self):
        # Before moving on, we need to check if any potential motion operation
        # is complete and remove it from active status.
        # NOTE: is_motion_complete should check children for completeness.
        if self._active_motion_op and self.is_motion_op_complete:
            self.clear_active_motion_op()

        if not self._active_motion_op and self.motion_ops:
            # Go get the next motion operation from the stack.
            self.motion_ops.reverse()
            self._active_motion_op = self.motion_ops.pop()
            self.motion_ops.reverse()
            # Push the motion op down to the child
            self.disperse_motion_op(self._active_motion_op)

        self.on_tick()

        if self.__dict__[self.CHILD_PROPERTY]:
            if not self.__dict__[self.CHILD_PROPERTY].is_motion_op_complete:
                self.__dict__[self.CHILD_PROPERTY].tick()

    def on_tick(self):
        pass
