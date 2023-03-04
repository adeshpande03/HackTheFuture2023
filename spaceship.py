MAX_SPEED = 10
MIN_SPEED = 3


class Spaceship:
    def __init__(self, mass=20, speed=3, boost = 0):
        self.lives = 3
        self.speed = speed
        self.mass = mass
        self.boost = boost
        
    def update_lives(self):
        if self.lives - 1 > -1:
            self.lives -= 1

    def update_speed(self, increase):
        if self.speed + increase <= MAX_SPEED:
            self.speed += increase
        else:
            self.speed = MAX_SPEED

    def update_mass(self, increase):
        self.mass += increase

    def get_boost_percentage(self):
        return (self.speed - MIN_SPEED) / MAX_SPEED
