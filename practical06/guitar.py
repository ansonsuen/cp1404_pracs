from datetime import datetime


class Guitar:
    """Represent a guitar"""
    def __init__(self, name='', cost=0, year=0):
        """Constrct a guitar object with name ,cost  and year"""
        self.name = name
        self.cost = cost
        self.year = year

    def __str__(self):
        """Return a sting representation of the guitar object"""
        output = "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)
        return output

    def get_age(self):
        """Return the age based on the current year grabbed from the system"""
        return datetime.now().year - self.year

    def is_vintage(self):
        """Determine whether a guitar is vintage based on age"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year



