import moco.motion_ops.base
import moco.attachment
import moco.motion_handler


class LinearAxis(moco.motion_handler.MotionHandler):

    CHILD_PROPERTY = 'attachment'

    def __init__(self, attachment: moco.attachment.Attachment=None):
        super(LinearAxis, self).__init__()

        self.attachment = attachment

    def on_tick(self):
        print('LinearAxis')
