class Attachment:
    def __init__(self):
        self.position = 0.0
        self.perfect_position = 0.0

    def move(self, distance):
        self.position += distance
        self.perfect_position += distance
