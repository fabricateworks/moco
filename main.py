import threading

# import pyglet
import moco.attachment
import moco.linear_axis
import moco.config
import moco.system.rate_limiter
import moco.motors.servo
import moco.motion_ops.linear_distance


# class GuiApplication(pyglet.window.Window):
#
#     def __init__(self):
#         super(GuiApplication, self).__init__()
#         pyglet.clock.schedule_interval(self.update, 1 / moco.config.HERTZ)
#
#         global control
#         self.control = control
#
#         self.motor_rotation = pyglet.text.Label(font_size=10, x=10, y=10)
#         self.motor_speed = pyglet.text.Label(font_size=10, x=10, y=20)
#
#     def update(self, dt):
#         pass
#
#     def on_draw(self):
#         self.clear()
#
#         self.motor_rotation.text = 'Motor Rotation: %s' % self.control.motor.rotary_encoder.rotation
#         self.motor_rotation.draw()
#
#         self.motor_speed.text = 'Motor Speed: %s RPM' % self.control.motor.speed
#         self.motor_speed.draw()
#
#     def on_text(self, text):
#         if text == '+':
#             self.control.motor.set_speed(self.control.motor.speed + 10)
#         if text == '-':
#             self.control.motor.set_speed(self.control.motor.speed - 10)
#
#     def start(self):
#         pyglet.app.run()


class MainLoop(moco.system.rate_limiter.RateLimiter):

    def tick(self):
        global control
        control.tick()


class Control:

    def __init__(self):
        self.attachment = moco.attachment.Attachment()
        self.x_axis = moco.linear_axis.LinearAxis(attachment=self.attachment)

        move0 = moco.motion_ops.linear_distance.LinearDistance(distance=100)
        self.x_axis.queue_motion_op(move0)

    def tick(self):
        self.x_axis.tick()


class ControlThread(threading.Thread):

    def run(self):
        MainLoop(moco.config.HERTZ).start()


control = Control()
ControlThread().start()
# GuiApplication().start()
