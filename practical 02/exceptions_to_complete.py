finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a number:"))
        print(result)
        finished = True
    except ValueError:  # TODO - add something after except
        print("Oops!  That was no valid number.  Try again...")
print("Valid result is ", result)

