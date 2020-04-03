MINIMUM_LENGTH = 4


def password_check():
    """Get a password of valid size and print asterisks."""
    password = input("Enter at least {} characters for password".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter at least {} characters for password".format(MINIMUM_LENGTH))
    print("*" * len(password))


password_check()