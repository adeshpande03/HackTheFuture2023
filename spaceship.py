MAX_SPEED = 10
MIN_SPEED = 3

class Spaceship:
    def __init__(self, mass=20, speed=3):
        self.lives = 3
        self.speed = speed
        self.mass = mass
        self.score = 0
        self.boost = 0
        
    def update_lives(self):
        if self.lives - 1 > -1:
            self.lives-=1
    def gain_mass(self):
        self.mass += 10
    
    def gain_boost(self):
        if self.boost == 100:
            return
        else:
            self.boost += 25

    def update_speed(self, increase):
        if self.speed + increase <= MAX_SPEED:
            self.speed += increase
        else:
            self.speed = MAX_SPEED

    def update_mass(self, increase):
        self.mass += increase

    def get_boost_percentage(self):
        return (self.speed-MIN_SPEED)/MAX_SPEED

    def update_score(self, increase):
        self.score += 1