import sys
import os
from operator import itemgetter


cwd = os.getcwd()
employees = {
#"ID":["NAME","STREET","CITY","STATE","ZIP","SSN","DOB","JOB","START","END"]
}
prompt = "\n HR SYSTEM OPTION MENU"
prompt += "\n Press 1: 'Display all employees'"
prompt += "\n Press 2: 'Display current employees'"
prompt += "\n Press 3: 'Display past employees'"
prompt += "\n Press 4: 'Add new employee'"
prompt += "\n Press 5: 'Edit employee record'"
prompt += "\n Press 6: 'Exit program'"
prompt += "\n Type '1','2','3','4','5','6' or '7' then hit Enter:"


def read_csv():
    with open(cwd + "\\" + "hr_records.csv", "r") as input_file:
        for line in input_file:
            create_database(line)
    return employees


def create_database(line):
    line = line.replace("\n", "") # Removes end of row delimited by "\n"
    line_list = line.split(",") # A row ends with "\n"
    employees[line_list[0]]=line_list[1:]


def create_list(line):
    list = line.split(",")
    print(list)
    return list


def display_all_employees():
    table = "\n"
    for k,v in employees.items():
        table += "{:^3}".format(k) + "|"
        for i in range (len(v)):
            if i == len(v)-1: # END
                table += "{:^10}".format( v[i][:10] ) + "\n"
            elif i == 0 or i == 2: # NAME or CITY
                table += "{:^10}".format( v[i][:10] ) + "|"
            elif i == 1: # STREET
                table += "{:^20}".format( v[i][:20] ) + "|"
            elif i == 3 or i ==4: # STATE or ZIP
                table += "{:^7}".format( v[i][:5] ) + "|"
            elif i == 5 or i == 6 or i == 8: # SSN or DOB or START
                table += "{:^13}".format( v[i][:13] ) + "|"
            elif i == 7: # JOB
                table += "{:^20}".format( v[i][:20] ) + "|"
    print (table)


def display_current_employees():
    table = "\n"
    for k,v in employees.items():
        if v[-1].lower() == "active" or v[-1].lower() == "end":
            table += "{:^3}".format(k) + "|"
            for i in range (len(v)):
                if i == len(v)-1: # END
                    table += "{:^10}".format( v[i][:10] ) + "\n"
                elif i == 0 or i == 2: # NAME or CITY
                    table += "{:^10}".format( v[i][:10] ) + "|"
                elif i == 1: # STREET
                    table += "{:^20}".format( v[i][:20] ) + "|"
                elif i == 3 or i ==4: # STATE or ZIP
                    table += "{:^7}".format( v[i][:5] ) + "|"
                elif i == 5 or i == 6 or i == 8: # SSN or DOB or START
                    table += "{:^13}".format( v[i][:13] ) + "|"
                elif i == 7: # JOB
                    table += "{:^20}".format( v[i][:20] ) + "|"
    print (table)


def display_past_employees():
    table = "\n"
    for k,v in employees.items():
        if "active" not in v[-1].lower() or v[-1].lower() == "end":
            table += "{:^3}".format(k) + "|"
            for i in range (len(v)):
                if i == len(v)-1: # END
                    table += "{:^10}".format( v[i][:10] ) + "\n"
                elif i == 0 or i == 2: # NAME or CITY
                    table += "{:^10}".format( v[i][:10] ) + "|"
                elif i == 1: # STREET
                    table += "{:^20}".format( v[i][:20] ) + "|"
                elif i == 3 or i ==4: # STATE or ZIP
                    table += "{:^7}".format( v[i][:5] ) + "|"
                elif i == 5 or i == 6 or i == 8: # SSN or DOB or START
                    table += "{:^13}".format( v[i][:13] ) + "|"
                elif i == 7: # JOB
                    table += "{:^20}".format( v[i][:20] ) + "|"
    print (table)

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
    new_id= len(employees.keys()) # Considers that first key is the title
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
        "1":display_all_employees,
        "2":display_current_employees,
        "3":display_past_employees,
        "4":add_employee,
        "5":edit_employee,
        "6":salir,
    }
    read_csv() # Create a database based on existing file
    while True:
        try:
            main_d[input(prompt)]()
        except KeyError:
            print("Not a valid option!")


if __name__ == "__main__":
    main()
