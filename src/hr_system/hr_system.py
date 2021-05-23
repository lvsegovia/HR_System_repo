import sys
import os
from operator import itemgetter
#import pyinputplus as inpt

cwd = os.getcwd()
employees = {
# Format:
# "ID":["NAME","STREET","CITY","STATE","ZIP","SSN","DOB","JOB","START","END"]
}
fields = { # Used to convert fields to list
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

header_break = "-"*3 + " "*2 + "-"*10 + " "*2 + "-"*20 + " "*2 + "-"*10 + " "*2 +\
"-"*7 + " "*2 + "-"*7 + " "*2 + "-"*13 + " "*2 + "-"*13 + " "*2 + "-"*20 +\
" "*2 + "-"*13 + " "*2 + "-"*10 + " "*2
unwanted_chars = [
    ".",
    ",",
    ":",
    "!",
    "?",
    "*",
    "$",
    "(",
    ")",
    "-",
    "'",
    '"',
    ";",
    "@",
    "[",
    "]",
    "+",
    "-",
    "#",
    "%",
    "^",
    "&",
    "=",
    "_",
    "`",
    "/",
    "|",
    "{",
    "}",
    "\\", # Backslash has to be doubled
]
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


def display_all_employees():
    # "ID":["NAME","STREET","CITY","STATE","ZIP","SSN","DOB","JOB","START","END"]
    print("\n")
    for k,v in employees.items():
        name,street,city,state,zip,ssn,dob,job,start,end = v
        print ("{:^5}{:^12}{:^22}{:^12}{:^9}{:^9}{:^15}{:^15}{:^22}{:^15}{:^12}\
        ".format(k,name,street,city,state,zip,ssn,dob,job,start,end))
        if k == "ID":
            print(header_break)
    while True:
        report_msg = input("\nDo you want a csv report? 'y' or 'n': ")
        try:
            report_msg.lower() == "y" or report_msg.lower() == "n"
        except False:
            continue
        if report_msg.lower() == "y":
            report_all_csv()
            break
        elif report_msg.lower() == "n":
            break
        print("type only 'y' or 'n' ")
        continue


def display_current_employees():
    # "ID":["NAME","STREET","CITY","STATE","ZIP","SSN","DOB","JOB","START","END"]
    print("\n")
    for k,v in employees.items():
        if v[-1].lower() == "active" or v[-1].lower() == "end":
            name,street,city,state,zip,ssn,dob,job,start,end = v
            print ("{:^5}{:^12}{:^22}{:^12}{:^9}{:^9}{:^15}{:^15}{:^22}{:^15}{:^12}\
            ".format(k,name,street,city,state,zip,ssn,dob,job,start,end))
            if k == "ID":
                print(header_break)
    while True:
        report_msg = input("\nDo you want a csv report? 'y' or 'n': ")
        try:
            report_msg.lower() == "y" or report_msg.lower() == "n"
        except False:
            continue
        if report_msg.lower() == "y":
            report_current_csv()
            break
        elif report_msg.lower() == "n":
            break
        print("type only 'y' or 'n' ")
        continue


def display_past_employees():
    # "ID":["NAME","STREET","CITY","STATE","ZIP","SSN","DOB","JOB","START","END"]
    print("\n")
    for k,v in employees.items():
        if "active" not in v[-1].lower() or v[-1].lower() == "end":
            name,street,city,state,zip,ssn,dob,job,start,end = v
            print ("{:^5}{:^12}{:^22}{:^12}{:^9}{:^9}{:^15}{:^15}{:^22}{:^15}{:^12}\
            ".format(k,name,street,city,state,zip,ssn,dob,job,start,end))
            if k == "ID":
                print(header_break)
    while True:
        report_msg = input("\nDo you want a csv report? 'y' or 'n': ")
        try:
            report_msg.lower() == "y" or report_msg.lower() == "n"
        except False:
            continue
        if report_msg.lower() == "y":
            report_past_csv()
            break
        elif report_msg.lower() == "n":
            break
        print("type only 'y' or 'n' :")
        continue


def add_employee():
    msg_name = clean_name()
    msg_street = clean_street()
    msg_city = clean_city()
    msg_state = clean_state()
    msg_zip = clean_zip()
    msg_ssn = clean_ssn()
    msg_dob = clean_dob()
    msg_job = clean_job() # Pending what to do
    msg_start = clean_start()
    msg_end = clean_end()
    new_id= str(len(employees.keys())) # Considers that first key is the title, adds to end
    employees[new_id]=[ msg_name,msg_street,msg_city,msg_state,msg_zip,
    msg_ssn,msg_dob,msg_job,msg_start,msg_end ]
    # Format to write in csv
    line = ""
    unwanted_chars = ["[","]","'"]
    line += str(employees[new_id])
    for i in unwanted_chars:
        line = line.replace(i, "")
    line = str(new_id)+","+ line + "\n"
    append_csv(line)


def clean_name():
    msg_name = input("\nType NAME: ")
    for i in unwanted_chars: # Removes unwanted chars from list
        msg_name = msg_name.replace(i, "")
    list_name = msg_name.split(" ")
    clean_name = ""
    for name in list_name:
        clean_name += name.capitalize() + " "
    clean_name = clean_name.strip() # Removes leading and trailing spaces
    return(clean_name)


def clean_street():
    msg_street = input("\nType STREET: ")
    for i in unwanted_chars: # Removes unwanted chars from list
        msg_street = msg_street.replace(i, "")
    return(msg_street)


def clean_city():
    msg_city = input("\nType CITY: ")
    for i in unwanted_chars: # Removes unwanted chars from list
        msg_city = msg_city.replace(i, "")
    clean_city = "".join(msg_city.split()) # Remove multiple spaces and last
    clean_city = clean_city.capitalize()
    return(clean_city)


def clean_state():
    while True: # Validate STATE
        msg_state = input("\nType STATE (must be 2 char, example 'WA'): ")
        try:
            len(msg_state.lower()) == 2
        except False:
            continue
        if len(msg_state.lower()) == 2 and msg_state[0].isdigit() == False and msg_state[1].isdigit()==False:
            break
        print("type only 2 characters, no numbers allowed :")
        continue
    return (msg_state)


def clean_zip():
    while True:  # Validate ZIP
        msg_zip = input("\nType ZIP (must be 5 numbers): ")
        try:
            int(msg_zip)
        except NameError:
            continue
        except ValueError:
            continue
        if len(msg_zip) == 5:
            break
        print("Zip code must be 5 numbers :")
        continue
    return (msg_zip)


def clean_ssn():
    while True:  # Validate SSN
        msg_ssn = input("\nType SSN (format must be 'XXX-XX-XXXX'): ")
        try:
            for i in range(11):
                if i <= 2 or i >=7:
                    int(msg_ssn[i])
                elif i == 4 or i ==5:
                    int(msg_ssn[i])
                elif i==3:
                    char_ssn3= msg_ssn[i]
                elif i==6:
                    char_ssn6= msg_ssn[i]
        except NameError:
            continue
        except ValueError:
            continue
        except IndexError:
            continue
        if len(msg_ssn) == 11 and char_ssn3 == "-" and char_ssn6 == "-":
            break
        print("Format = (3 numbers '-' 2 numbers '-' 4 numbers): ")
        continue
    return (msg_ssn)


def clean_dob():
    while True:  # Validate DOB
        msg_dob = input("\nType DOB (format must be 'MMM/DD/YYYY'): ")
        try:
            for i in range(11):
                if i == 4 or i ==5:
                    int(msg_dob[i])
                elif i >= 7:
                    int(msg_dob[i])
        except NameError:
            continue
        except ValueError:
            continue
        except IndexError:
            continue
        if len(msg_dob) == 11 and msg_dob[3] == "/" and msg_dob[6] == "/" and msg_dob[0].isdigit() == False and msg_dob[1].isdigit() == False and msg_dob[2].isdigit() == False:
            break
        print("Format example = (3 letters('sep') '/' 2 numbers('10') '/' 4 numbers(1984)): ")
        continue
    return(msg_dob)


def clean_job():
    msg_job = input("\nType JOB: ")
    return(msg_job.upper())


def clean_start():
    while True:  # Validate START date
        msg_start = input("\nType START date (format must be 'MMM/DD/YYYY'): ")
        try:
            for i in range(11):
                if i == 4 or i ==5:
                    int(msg_start[i])
                elif i >= 7:
                    int(msg_start[i])
        except NameError:
            continue
        except ValueError:
            continue
        except IndexError:
            continue
        if len(msg_start) == 11 and msg_start[3] == "/" and msg_start[6] == "/" and msg_start[0].isdigit() == False and msg_start[1].isdigit() == False and msg_start[2].isdigit() == False:
            break
        print("Format example = (3 letters('feb') '/' 2 numbers('08') '/' 4 numbers(2008)): ")
        continue
    return(msg_start)


def clean_end():
    while True:
        active_msg = input("\nIs employee active? 'y' or 'n': ")
        try:
            active_msg.lower() == "y" or active_msg.lower() == "n"
        except False:
            continue
        if active_msg.lower() == "y":
            msg_end="active".upper()
            break
        elif active_msg.lower() == "n":
            ######## Loop for terminated employee
            while True:  # Validate END date
                msg_end = input("\nType END date (format must be 'MMM/DD/YYYY') : ")
                try:
                    for i in range(11):
                        if i == 4 or i ==5:
                            int(msg_end[i])
                        elif i >= 7:
                            int(msg_end[i])
                except NameError:
                    continue
                except ValueError:
                    continue
                except IndexError:
                    continue
                if len(msg_end) == 11 and msg_end[3] == "/" and msg_end[6] == "/" and msg_end[0].isdigit() == False and msg_end[1].isdigit() == False and msg_end[2].isdigit() == False:
                    break
                print("Format example = (3 letters('feb') '/' 2 numbers('08') '/' 4 numbers(2008)): ")
                continue
            #########
            break
        print("type only 'y' or 'n' :")
        continue
    return (msg_end)


def show_id_name():
    table = "\n"
    for k,v in employees.items():
        table += "{:^3}".format(k) + "|"
        table += "{:^10}".format( v[0][:10] ) + "|" + "\n"
    print (table)


def edit_employee():
    show_id_name()
    while True:  # Validate START date
        msg_id = input("\nSelect employee ID to edit: ")
        try:
            employees[msg_id]
            break
        except KeyError:
            print("Select existing employee")
            continue
        except ValueError:
            continue
        except IndexError:
            continue
        continue
    while True:
        msg_field = input("""'NAME','STREET','CITY','STATE','ZIP','SSN','DOB','JOB','START','END'
    Type field to edit: """)
        try:
            fields[msg_field.lower()]
            break
        except KeyError:
            print("Type valid field")
            continue
        continue
    msg_value = fields_fun[msg_field]() # Clean the data using dictionary accordingly
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

fields_fun = { # Assings funtions to fields
"name":clean_name,
"street":clean_street,
"city":clean_city,
"state":clean_state,
"zip":clean_zip,
"ssn":clean_ssn,
"dob":clean_dob,
"job":clean_job,
"start":clean_start,
"end":clean_end,
}

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
