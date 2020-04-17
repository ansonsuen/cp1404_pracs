import random

MINIMUM = 1
MAXIMUM = 45

NUMBERS_PER_LINE = 6


def main():
    """Quick picks program - choose sets of random numbers."""
    number_of_quick_picks = int(input("how many quick picks do you wish to generate: "))
    while number_of_quick_picks < 0:
        print("it does not make sense")
        number_of_quick_picks = int(input("how many quick picks do you wish to generate: "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))


if __name__ == '__main__':
    main()
