"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly."""
    data = get_data()
    display_subjects(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data=[]
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts, end=' ,')  # See if that worked
        data.append(parts)
    input_file.close()
    return data


def display_subjects(data):
    """Display data nicely."""
    for subject_data in data:
        print("{} is taught by {} Lovelace and has {}students".format(*subject_data))


main()
