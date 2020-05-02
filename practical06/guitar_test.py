from practical06.guitar import Guitar


def run_unqiue_test():
    """Tests for Guitar class."""
    guitar = Guitar("Gibson L-5 CES", 1992, 16035.40)
    another_guitar = Guitar("Another Guitar", 2010, 909)
    print("{} get_age {} - Expected 98. Got {}".format(guitar.name, 95,guitar.get_age()))

    print("{} get_age {} - Expected 98. Got {}".format(another_guitar.name, 5,another_guitar.get_age()))
    print("{} is vintage ()gu- Expected True. Got {}".format(guitar.name, guitar.is_vintage()))
    print("{} is vintage ()- Expected True. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


if __name__ == '__main__':
    run_unqiue_test()
