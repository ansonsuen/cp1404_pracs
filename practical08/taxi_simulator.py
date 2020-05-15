from practical08.car import Car
from practical08.taxi import Taxi
from practical08.silver_service_taxi import SilverServiceTaxi


def menu():
    print("q)uit, c)hoose taxi, d)rive")


def display_taxi(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{}-{}".format(i, taxi))


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    menu()
    choice_menu = str(input(""))
    while choice_menu != "q".lower():
        if choice_menu == "c":
            print("Taxis available:")
            display_taxi(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif choice_menu == "d":
            current_taxi.start_fare()
            drive_distance = float(input("Drive how far? "))
            current_taxi.drive(drive_distance)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                         trip_cost))
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(menu())
        choice_menu = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxi(taxis)


def run_tests():
    """Run tests to show workings of Car and Taxi classes."""
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)
    print(bus)

    # drive bus (input/loop is oblivious to fuel)
    distance = int(input("Drive how far? "))
    while distance > 0:
        travelled = bus.drive(distance)
        print("{} travelled {}".format(str(bus), travelled))
        distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


if __name__ == '__main__':
    main()
