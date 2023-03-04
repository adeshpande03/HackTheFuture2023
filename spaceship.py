SPEED = 3


class Spaceship:
    def __init__(self, mass=20):
        self.lives = 3
        self.speed = SPEED
        self.mass = mass

    def update_lives(self):
        if self.lives - 1 > -1:
            self.lives -= 1

    def update_speed(self, increase):
        self.speed += increase

    def update_mass(self, increase):
        self.mass += increase
