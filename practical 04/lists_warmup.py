def lst_of_numbers():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    # numbers[0] =[3]
    # numbers[-1]=[2]
    # numbers[3]= [1]
    # numbers[:-1]=[3, 1, 4, 1, 5, 9]
    # numbers[3:4]= [1]
    # 5 in numbers = True
    # 7 in numbers= False
    # "3" in numbers= False
    print(numbers + [6, 5, 3])


lst_of_numbers()


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(
            input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print report based on incomes."""
    # Note that we do not need to pass in number_of_months
    # because we know the length of the incomes list
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(month + 1, income, total))


main()
