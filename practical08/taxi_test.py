from practical08.taxi import Taxi


def main():
    # create a new taxi with name"Prius 1" , 100 units of fuel and price of $1.23
    prius_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40km
    prius_taxi.drive(40)

    # Print the taxi's details and current fare
    print(prius_taxi)

    # Restart the meter (start a new fare) and then drive the car 100km
    prius_taxi.start_fare()
    prius_taxi.drive(100)

    # Print the taxi's details and current fare
    print(prius_taxi)
    print("Current fare:${:.2f}".format(prius_taxi.get_fare()))


if __name__ == '__main__':
    main()
