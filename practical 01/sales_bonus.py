def main():
    sales = float(input("Enter sales: $"))
    if sales < 1000:
        total = sales * 0.1
    else:
        total = sales * 0.15
    return print("Bonus is $", total, sep='')


if __name__ == '__main__':
    main()

