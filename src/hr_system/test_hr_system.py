import sys
import os
import hr_system
from datetime import date

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
    "\\",
]

states_dic = {  # Assings funtions to clean fields
    "al": "alabama",
    "ak": "alaska",
    "as": "american samoa",
    "az": "arizona",
    "ar": "arkansas",
    "ca": "california",
    "co": "colorado",
    "ct": "connecticut",
    "de": "delaware",
    "dc": "district of columbia",
    "fl": "florida",
    "ga": "georgia",
    "guam": "gu",
    "hi": "hawaii",
    "id": "idaho",
    "il": "illinois",
    "in": "indiana",
    "ia": "iowa",
    "ks": "kansas",
    "ky": "kentucky",
    "la": "louisiana",
    "me": "maine",
    "md": "maryland",
    "ma": "massachusetts",
    "mi": "michigan",
    "mn": "minnesota",
    "ms": "mississippi",
    "mo": "missouri",
    "mt": "montana",
    "ne": "nebraska",
    "nv": "nevada",
    "nh": "new hampshire",
    "nj": "new jersey",
    "nm": "new mexico",
    "ny": "new york",
    "nc": "north carolina",
    "nd": "norht dakota",
    "mp": "northern mariana is",
    "oh": "ohio",
    "ok": "oklahoma",
    "or": "oregon",
    "pa": "pennsylvania",
    "pr": "puerto rico",
    "ri": "rhode island",
    "sc": "south carolina",
    "sd": "south dakota",
    "tn": "tennessee",
    "tx": "texas",
    "ut": "utah",
    "vt": "vermont",
    "va": "virginia",
    "vi": "virgin islands",
    "wa": "washington",
    "wv": "west virginia",
    "wi": "wisconsin",
    "wy": "wyoming",
}

month_dic = {
    "jan": ["january", "01"],
    "feb": ["february", "02"],
    "mar": ["march", "03"],
    "apr": ["april", "04"],
    "may": ["may", "05"],
    "jun": ["june", "06"],
    "jul": ["july", "07"],
    "aug": ["august", "08"],
    "sep": ["september", "09"],
    "oct": ["october", "10"],
    "nov": ["november", "11"],
    "dec": ["december", "12"],
}


def test_read_csv():
    employees = hr_system.read_csv()
    assert employees["ID"] == ["NAME","STREET","CITY","STATE","ZIP","SSN","DOB","JOB","START","END"]


def test_create_database():
    dic = hr_system.create_database('leo,name,street,city,state,zip,ssn,dob,job,start,end')
    assert dic['leo'] == ['name','street','city','state','zip','ssn','dob','job','start','end']


def test_unwanted_chars_fun():
    string1 = hr_system.unwanted_chars_fun("t^h!i@s#$ i*s% a t:e+s-t")
    assert string1 =="this is a test"


def test_capitalize_sentence():
    string2 = hr_system.capitalize_sentence('this test')
    assert string2 == 'This Test'


def test_no_spaces_capitalize():
    text = hr_system.no_spaces_capitalize(" sea ttle ")
    assert "Seattle" == text

#this thest will work only MAY or JUN 2021 and if no new entris that END last month
def test_display_past_month_employees():
    test_table = "\n"+\
    " 6 |      Cynthia       |  apr/27/2021  |\n"+\
    " 7 |        Neil        |  apr/27/2021  |\n"+\
    "12 |   Tony Simonelli   |  may/20/2021  |\n"
    string1 = hr_system.display_past_month_employees()[0]
    string2 = hr_system.display_past_month_employees()[1]
    if_may = "The employees that left last MAY 2021 :"
    if_jun = "The employees that left last JUN 2021 :"
    assert string1 == test_table
    assert string2 == if_may or string2 == if_jun


#this thest will work only if no new entries within next 3 months
def test_review_reminder():
    test_reminder = "\n" + "*" * 100 + \
    "\nDue for review employees: \n" + \
    " 3 |       Nahim        |    jun/06     |\n"+ \
    " 8 |       Robert       |    jul/04     |\n"+ \
    "19 |    Walter White    |    aug/15     |\n"+ \
    "20 |   Jesse Pinkman    |    may/26     |\n"+ \
    "22 |    Jim Reynolds    |    jul/13     |\n"
    string1 = hr_system.review_reminder()
    assert test_reminder == string1
