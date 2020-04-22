"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)


def main():
    """asks the user for their 'short' state """
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        if state_code in CODE_TO_NAME:
            print("{:3} is {:12}".format(state_code, CODE_TO_NAME[state_code]))
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()


if __name__ == '__main__':
    main()
