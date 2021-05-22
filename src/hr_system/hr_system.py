import sys
import os
from operator import itemgetter


cwd = os.getcwd()
prompt = "\n HR SYSTEM OPTION MENU"
prompt += "\n Press 1: 'Display current employees'"
prompt += "\n Press 2: 'Add new employee'"
prompt += "\n Press 3: 'Edit employee'"
prompt += "\n Press 4: 'List of past employees'"
prompt += "\n Press 5: 'Exit program'"
prompt += "\n Type here: "


def read_csv():
    content=""
    with open(cwd + "\\" + "hr_records.csv", "r") as input_file:
        for line in input_file:
            print(line)
            content += line
    return content


def display_employees():
    print("Content is\n" + read_csv())



def add_employee():
    print("add")
    pass


def edit_employee():
    print("edit")
    pass


def list_past_employee():
    print("past")
    pass


def salir():
    sys.exit()


def main():
    main_d = {
        "1":display_employees,
        "2":add_employee,
        "3":edit_employee,
        "4":list_past_employee,
        "5":salir,
    }
    while True:
        try:
            main_d[input(prompt)]()
        except KeyError:
            print("Not a valid option!")


if __name__ == "__main__":
    main()
