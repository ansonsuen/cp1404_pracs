def convert_celsius_to_fahrenheit(celsius):
    """"convert  Celsius to Fahrenheit"""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


MENU = """
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """conversion program of temperature"""
    print(MENU)
    choice = str(input(">>>")).upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result:{:.2f}".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result:{:.2f}".format(celsius))
        else:
            print("invalid")
        print(MENU)
        choice = str(input(">>>"))
    print("thank You")


if __name__ == '__main__':
    main()
