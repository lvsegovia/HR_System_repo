import sys
import os
from operator import itemgetter


cwd = os.getcwd()
employees = {
# Format:
# "ID":["NAME","STREET","CITY","STATE","ZIP","SSN","DOB","JOB","START","END"]
}
fields = {
"name":0,
"street":1,
"city":2,
"state":3,
"zip":4,
"ssn":5,
"dob":6,
"job":7,
"start":8,
"end":9,
}
prompt = "\n HR SYSTEM OPTION MENU"
prompt += "\n Press 1: 'Display all employees'"
prompt += "\n Press 2: 'Display current employees'"
prompt += "\n Press 3: 'Display past employees'"
prompt += "\n Press 4: 'Add new employee'"
prompt += "\n Press 5: 'Edit employee record'"
prompt += "\n Press 6: 'Exit program'"
prompt += "\n Type '1','2','3','4','5' or '6' then hit Enter:"


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
    report_msg = input("Do you want a csv report?, y/n: ")
    if report_msg.lower() == "y":
        report_all_csv()


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
    report_msg = input("Do you want a csv report?, y/n: ")
    if report_msg.lower() == "y":
        report_current_csv()


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
    report_msg = input("Do you want a csv report?, y/n: ")
    if report_msg.lower() == "y":
        report_past_csv()


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
    new_id= len(employees.keys()) # Considers that first key is the title, adds to end
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
    line += str(employees[new_id])
    for i in unwanted_chars:
        line = line.replace(i, "")
    line = str(new_id)+","+ line + "\n"
    append_csv(line)


def show_id_name():
    table = "\n"
    for k,v in employees.items():
        table += "{:^3}".format(k) + "|"
        table += "{:^10}".format( v[0][:10] ) + "|" + "\n"
    print (table)

def edit_employee():
    show_id_name()
    msg_id = input("\nSelect employee ID to edit: ")
    msg_field = input("""'NAME','STREET','CITY','STATE','ZIP','SSN','DOB','JOB','START','END'
    Type field to edit: """)
    msg_value = input("""\n Type new value: """)
    employees[msg_id][ fields[msg_field.lower()] ] = msg_value
    update_csv()


def list_past_employee():
    print("past")
    pass


def report_all_csv():
    with open(cwd + "\\" + "hr_report.csv", "w") as file:
        content = ""
        for k,v in employees.items():
            content += k + ","
            for i in range (len(v)):
                if i == (len(v)-1):
                    content += v[i] + "\n"
                else:
                    content += v[i] + ","
        file.write(content)



def report_current_csv():
    with open(cwd + "\\" + "hr_report.csv", "w") as file:
        content = ""
        for k,v in employees.items():
            if v[-1].lower() == "active" or v[-1].lower() == "end":
                content += k + ","
                for i in range (len(v)):
                    if i == (len(v)-1):
                        content += v[i] + "\n"
                    else:
                        content += v[i] + ","
        file.write(content)


def report_past_csv():
    with open(cwd + "\\" + "hr_report.csv", "w") as file:
        content = ""
        for k,v in employees.items():
            if "active" not in v[-1].lower() or v[-1].lower() == "end":
                content += k + ","
                for i in range (len(v)):
                    if i == (len(v)-1):
                        content += v[i] + "\n"
                    else:
                        content += v[i] + ","
        file.write(content)


def update_csv(): # Converts employees to csv format
    with open(cwd + "\\" + "hr_records.csv", "w") as file:
        content = ""
        for k,v in employees.items():
            content += k + ","
            for i in range (len(v)):
                if i == (len(v)-1):
                    content += v[i] + "\n"
                else:
                    content += v[i] + ","
        file.write(content)


def append_csv(line): # Entry line must be in csv format
    with open(cwd + "\\" + "hr_records.csv", "a") as file:
        file.write(line)


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
