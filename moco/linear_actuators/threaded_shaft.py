import weakref


class ThreadedShaft:

    def __init__(self):
        self._distance_per_rotation = 1000
        self._attachment = None

    def rotate(self, amount):
        distance = amount * self._distance_per_rotation
        self.attachment.move(distance)

    @property
    def attachment(self):
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        self._attachment = weakref.proxy(attachment)
