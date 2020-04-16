# 1. Numbers stuff
numbers = []
for i in range(5):
    number = int(input("Number:"))
    numbers.append(number)
print("The first number is", numbers[0])
print("The last number is", numbers[4])
print("The smallest number is ", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers))

# 2. Woefully inadequate security checker...
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = str(input("Enter username"))
if username != usernames:
    print("Access denied")
else:
    print("Access granted")
