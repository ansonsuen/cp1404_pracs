"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly."""
    data = []
    load_data(data)
    display_subjects(data)


def load_data(data):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def display_subjects(data):
    """Display data nicely."""
    for subject_data in data:
        print("{} is taught by {:12} Lovelace and has {:3} students".format(*subject_data))


if __name__ == '__main__':
    main()
