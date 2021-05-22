import sys
import os
from operator import itemgetter


cwd = os.getcwd()
employees = {
#"ID":["NAME","STREET","CITY","STATE","ZIP","SSN","DOB","JOB","START","END"]
}
prompt = "\n HR SYSTEM OPTION MENU"
prompt += "\n Press 1: 'Display current employees'"
prompt += "\n Press 2: 'Add new employee'"
prompt += "\n Press 3: 'Edit employee'"
prompt += "\n Press 4: 'List of past employees'"
prompt += "\n Press 5: 'Exit program'"
prompt += "\n Type here: "


def read_csv():
    with open(cwd + "\\" + "hr_records.csv", "r") as input_file:
        for line in input_file:
            create_database(line)
    #print(employees)
    return employees


def create_database(line):
    line = line.replace("\n", "") # Removes end of row delimited by "\n"
    line_list = line.split(",") # A row ends with "\n"
    employees[line_list[0]]=line_list[1:]


def create_list(line):
    list = line.split(",")
    print(list)
    return list


def display_employees():
    print(employees)


def add_employee():
    msg_name = input("\nType NAME: ")
    msg_street = input("\nType STREET: ")
    msg_city = input("\nType CITY: ")
    msg_state = input("\nType STATE: ")
    msg_zip = input("\nType ZIP: ")
    msg_ssn = input("\nType SSN: ")
    msg_dob = input("\nType DOB: ")
    msg_job = input("\nType JOB: ")
    msg_start = input("\nType START: ")
    msg_end = input("\nType END: ")
    new_id= len(employees.keys()) # Taking into account that first key is the title
    employees[new_id]=[
    msg_name,
    msg_street,
    msg_city,
    msg_state,
    msg_zip,
    msg_ssn,
    msg_dob,
    msg_job,
    msg_start,
    msg_end
    ]
    line = ""
    unwanted_chars = ["[","]","'"]
    with open(cwd + "\\" + "hr_records.csv", "a") as input_file:
        line += str(employees[new_id])
        for i in unwanted_chars:
            line = line.replace(i, "")
        line = str(new_id)+","+ line + "\n"
        input_file.write(line)
    line = ""

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
    read_csv()
    while True:
        try:
            main_d[input(prompt)]()
        except KeyError:
            print("Not a valid option!")


if __name__ == "__main__":
    main()
