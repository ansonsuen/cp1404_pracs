"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    populate_income(incomes)
    print_report(incomes)


def populate_income(incomes):
    """Add income to income list from user input"""
    numbers_of_months = int(input("How many months? "))
    for month in range(1, numbers_of_months + 1):
        income = float(
            input("Enter income for month{}: ".format(month)))
        incomes.append(income)


def print_report(incomes):
    """Display income report for incomes based on income list."""

    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(month + 1, income, total))


main()