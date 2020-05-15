from practical08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Return a string representation of a SilverServiceTaxi."""

        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return "{} plus flag fall of ${:.2f}".format(super().__str__(),
                                                     self.flag_fall)

    def get_fare(self):
        """Get the current fare."""
        return self.flag_fall + super().get_fare()
