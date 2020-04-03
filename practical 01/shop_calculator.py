def main():
    number_of_item = int(input("Number of inputs:"))
    total_price = 0
    while number_of_item < 0:
        print("invalid number:")
        number_of_item = int(input())
    for i in range(number_of_item):
        price = float(input("Price of item:"))
        total_price += price
    if total_price > 100:
        total_price *= 0.9
        print("Total price for {} items is ${:.2f} ".format(number_of_item, total_price))
    else:
        print("Total price for {} items is ${:.2f} ".format(number_of_item, total_price))


if __name__ == '__main__':
    main()
