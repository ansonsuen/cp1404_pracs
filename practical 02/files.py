# 1
out_file = open('name.txt', 'w')
name = str(input("What is your name:"))
out_file.write(name)
print(name, file=out_file.close())
out_file.close()

# 2
in_file = open("name.txt", "r")
print("Your name is", name)
in_file.close()

# 3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)

in_file.close()
# 4
in_file = open("numbers.txt", "r")
total = 0
for numbers in in_file:
    number = int(numbers)
    total += number

in_file.close()
print(total)
