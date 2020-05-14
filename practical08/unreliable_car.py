from random import randint


class unreliable_car(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        driven_distance = super().__init__(distance)
        return driven_distance




