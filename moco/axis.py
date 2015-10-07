class Axis:
    def __init__(self):
        self.motor = Motor()
        self.motor.rotates = ThreadedShaft()
        self.motor.rotates.attachment = ThreadedAttachment()

        self.active_movement = None
        self.movement_queue = []

    def queue_movement(self, movement):
        self.movement_queue.append(movement)

    def _check_for_new_movement_operation(self):
        if not self.active_movement and self.movement_queue:
            self.movement_queue.reverse()
            self.active_movement = self.movement_queue.pop()
            self.movement_queue.reverse()

            number_of_rotations = self.active_movement.distance / self.motor.rotates.distance_per_rotation
            if number_of_rotations < 0:
                self.active_movement._normalized_direction_vector = -1
            else:
                self.active_movement._normalized_direction_vector = 1
            print('Will move %d rotation(s)' % number_of_rotations)
            self.active_movement._started_at['rotation'] = self.motor.perfect_rotation
            self.active_movement._started_at['position'] = self.motor.rotates.attachment.perfect_position
            self.active_movement._wait_for['rotation'] = self.motor.perfect_rotation + number_of_rotations
            self.active_movement._wait_for['position'] = self.motor.rotates.attachment.perfect_position + self.active_movement.distance
            print('Will wait for %s' % self.active_movement._wait_for)
            return True
        else:
            return False

    def tick(self):
        self._check_for_new_movement_operation()

        if self.active_movement:
            should_stop = False
            if self.active_movement._normalized_direction_vector < 0:
                should_stop = self.motor.rotation - self.active_movement._wait_for['rotation'] <= 0
            else:
                should_stop = self.active_movement._wait_for['rotation'] - self.motor.rotation <= 0
            if should_stop:
                self.motor.perfect_rotation = self.active_movement._wait_for['rotation']
                self.motor.rotates.attachment.perfect_position = self.active_movement._wait_for['position']
                self.motor.set_speed(0)
                self.active_movement = None
                print(self.motor.rotates.attachment.position)
            else:
                relative_position = abs(self.motor.rotates.attachment.position - self.active_movement._started_at['position'])
                speed_modifier = 1
                # Within acceleration zone
                if relative_position <= self.active_movement.acceleration_distance:
                    speed_modifier = relative_position / self.active_movement.acceleration_distance
                # Within deceleration zone
                elif abs(self.motor.rotates.attachment.position - self.active_movement._wait_for['position']) <= self.active_movement.deceleration_distance:
                    speed_modifier = (self.motor.rotates.attachment.position - self.active_movement._wait_for['position']) / self.active_movement.deceleration_distance
                speed_modifier = abs(speed_modifier)
                if speed_modifier < 0.01:
                    speed_modifier = 0.01
                self.motor.set_speed(self.active_movement.speed * speed_modifier * self.active_movement._normalized_direction_vector)
