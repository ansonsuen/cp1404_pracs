from practical06.car import Car

MENU = " Menu:\nd) drive\n r) refuel\n q) quit\n"


def main():
    """Car simulator program, demonstrating use of Car class."""
    print("Let's drive!")
    car_name = input("Enter your car name:")
    car = Car(car_name, 100)
    print(car)
    choice = input(" Enter your choice").lower()
    while choice != "q"():
        if choice == "d":
            drive_km = int(input("How many km do you wish to drive?"))
            while drive_km <= 0:
                print("Distance must be >= 0")
                drive_km = int(input("How many km do you wish to drive?"))
            drive_km = car.drive(drive_km)
            print(" The car drove {}km.".format(drive_km))
            if car.fuel == 0:
                print(" and ran out of fuel", end="")
                print(".")
        elif choice == "r":
            add_car_fuel = int(input("How many units of fuel do you want to add to the car?"))
            while add_car_fuel <= 0:
                print(" Fuel amount must be >= 0")
                add_car_fuel = int(input("How many units of fuel do you want to add to the car?"))
            car.add_fuel(add_car_fuel)


if __name__ == '__main__':
    main()
