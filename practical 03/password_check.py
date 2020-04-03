MINIMUM_LENGTH = 4


def password_check():
    """Get a password of valid size and print asterisks."""
    password = int(input("Enter at least {} characters for password".format(MINIMUM_LENGTH)))
    while password < MINIMUM_LENGTH:
        password = int(input("Enter at least {} characters for password".format(MINIMUM_LENGTH)))
    print("*" * len(password))


