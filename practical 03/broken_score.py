import random


def score_status_determination(score):
    """determine the grades of scores"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    """print status due to the score"""

    score = float(input("Enter score: "))

    print(score_status_determination(score))


if __name__ == '__main__':
    main()
