"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    student_infomation = print_student_infomation(FILENAME)
    display_subject_details(student_infomation)
    # print(student_infomation)


def print_student_infomation(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    nest = []
    for subject_data in input_file:
        print(subject_data)  # See what a line looks like
        print(repr(subject_data))  # See what a line really looks like
        subject_data = subject_data.strip()  # Remove the \n
        records = subject_data.split(',')  # Separate the data into its parts
        print(records)  # See what the parts look like (notice the integer is a string)
        records[2] = int(records[2])  # Make the number an integer (ignore PyCharm's warning)
        print(records)  # See if that worked
        nest.append(records)  # adding each parts of to list inside a list
        print("----------")
    print("below shows the nested data")
    print(nest)
    input_file.close()
    return nest

def display_subject_details(student_infomation):
    """Display subject details."""
    print("display subject details")
    # print(student_infomation)
    for records in student_infomation:
        subject = records[0]
        lecturer = records[1]
        student = records[2]
        print(f"{subject} is taught by {lecturer} and has {student} students")

main()
