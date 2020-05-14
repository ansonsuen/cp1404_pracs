from practical08.unreliable_car import Unreliable_Car


def main():
    """Test some UnreliableCars."""

    # create cars with different reliabilities
    good_car = Unreliable_Car("Mostly Good", 100, 90)
    bad_car = Unreliable_Car("Dodgy", 100, 9)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


if __name__ == '__main__':
    main()
