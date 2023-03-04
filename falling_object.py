class falling_object:
    def __init__(self, type, mass):
        self.type = type
        self.mass = mass

    def get_gravity(self, spaceship, r):
        return (spaceship.mass*self.mass)/r**2

    def is_heavier(self, spaceship):
        return spaceship.mass > self.mass