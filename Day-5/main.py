"""
    day - 5
"""
import sys
import datetime
import logging
import configparser
import json
from dateutil.relativedelta import relativedelta
import mysql.connector

logging.basicConfig(filename='Info.log', level=logging.INFO)


def print_json_response(response, rea):
    """
    printing json object
    """
    dict_json = {"response": response, "reason": rea}
    json_obj = json.dumps(dict_json)
    logging.info("Convert to json object")
    print(json_obj)


def validate_name(first_name_input, last_name_input):
    """
        validates first name and last name
    """
    logging.info("validating first name and last name")
    if len(first_name_input) == 0 or len(last_name_input) == 0:
        return "Invalid first name or last name"
    if not first_name_input.isalpha() or not last_name_input.isalpha():
        return "Invalid first name or last name"
    return "SUCCESS"


def validate_dob(dob_input):
    """
        validates date of birth
    """
    logging.info("validating date of birth")
    try:
        datetime.datetime.strptime(dob_input, '%Y-%m-%d')
        return "SUCCESS"
    except ValueError:
        return "Invalid input for DOB"


def validate_gender(gender_input):
    """
        validates gender
    """
    logging.info("validating gender")
    low_gender = gender_input.lower()
    if low_gender in ('male', 'female'):
        return "SUCCESS"
    return "Invalid input for gender"


def validate_nationality(nationality_input):
    """
        validates nationality
    """
    logging.info("validating nationality")
    if len(nationality_input) == 0 or not nationality_input.isalpha():
        return "Invalid input for nationality"
    return "SUCCESS"


def validate_current_city(current_city_input):
    """
        validates city
    """
    logging.info("validating city")
    if len(current_city_input) == 0 or not current_city_input.isalpha():
        return "Invalid input for current city"
    return "SUCCESS"


def validate_state(state_input):
    """
        validates state
    """
    logging.info("validating state")
    if len(state_input) != 0 and all(char.isalpha() or char.isspace() for char in state_input):
        return "SUCCESS"
    return "Invalid input for state"


def validate_pin_code(pin_code_input):
    """
        validates pin-code
    """
    logging.info("validating pin-code")
    if len(pin_code_input) == 6 and pin_code_input.isnumeric():
        return "SUCCESS"
    return "Invalid input for pin-code"


def validate_qualification(qualification_input):
    """
        validates qualification
    """
    logging.info("validating qualification")
    if len(qualification_input) == 0 or not qualification_input.isalpha():
        return "Invalid input for qualification"
    return "SUCCESS"


def validate_salary(salary_input):
    """
            validates salary
    """
    logging.info("validating salary")
    if len(salary_input) != 0 and salary_input.isnumeric() and int(salary_input) > 0:
        return "SUCCESS"
    return "Invalid input for salary"


def validate_pan(pan_input):
    """
            validates pan
    """
    logging.info("validating pan")
    if len(pan_input) == 10 and pan_input.isalnum():
        return "SUCCESS"
    return "Invalid input for pan"


class CheckEligibility:
    """
        checks eligibility criteria
    """

    # pylint: disable=too-many-instance-attributes
    def __init__(self, request_id_input, gender_input, age_input,
                 nationality_input, state_input, pan_input, salary_input):
        # pylint: disable=too-many-arguments
        self.request_id = request_id_input
        self.gender = gender_input.lower()
        self.age = age_input
        self.nationality = nationality_input.lower()
        self.state = state_input.lower()
        self.pan = pan_input
        self.salary = salary_input
        self.response = "SUCCESS"
        self.reason = ""

    def create_json_object(self):
        """
            create json object
        """
        dict_obj = {"request_id": self.request_id, "response": self.response}
        if self.reason != "":
            dict_obj["reason"] = self.reason
        json_obj = json.dumps(dict_obj)
        logging.info("Convert to json object")
        return json_obj

    def check_age(self):
        """
            check age eligibility
        """
        if self.gender == 'male' and self.age > 21:
            pass
        elif self.gender == 'female' and self.age > 18:
            pass
        else:
            self.reason = "Age does not meet eligibility criteria"
            self.response = "FAILED"
        logging.info("checking age eligibility")

    def check_nationality(self):
        """
            check nationality eligibility
        """
        if self.nationality not in ("indian", "american"):
            self.reason = "Nationality should be Indian or American"
            self.response = "FAILED"
        logging.info("checking nationality eligibility")

    def check_state(self):
        """
        check state eligibility
        """
        if self.state not in ("andhra pradesh", "arunachal pradesh", "assam", "bihar",
                              "chhattisgarh", "karnataka", "madhya pradesh",  "odisha",
                              "tamil nadu",  "telangana", "west bengal"):
            self.reason = "State does not meet eligibility criteria"
            self.response = "FAILED"
        logging.info("checking state eligibility")

    def check_salary(self):
        """
        check salary eligibility
        """
        if self.salary < 10000 or self.salary > 90000:
            self.reason = "Salary does not meet eligibility criteria"
            self.response = "FAILED"
        logging.info("checking salary eligibility")

    def check_pan(self, dbcursor, today):
        """
            check whether request is recieved in last 5 days
        """
        logging.info("checking whether request is recieved in last 5 days")
        query = "SELECT created_at FROM request where created_at != %s and pan = %s"
        value = (today, self.pan)
        dbcursor.execute(query, value)
        rows = dbcursor.fetchall()
        for row, value in enumerate(rows):
            logging.info("checking %s row from result in checking "
                         "that request is recieved in last 5 days", row)
            create = value[0]
            days = self.find_difference(today, str(create))
            if days <= 5:
                self.reason = "Recently request received in last 5 days"
                self.response = "FAILED"
                break

    def check_all(self, dbcursor, today):
        """
            call all methods
        """
        self.check_salary()
        self.check_pan(dbcursor, today)
        self.check_state()
        self.check_nationality()
        self.check_age()

    @staticmethod
    def find_difference(today, create):
        """
         find difference between two dates
        """
        logging.info("find difference between %s and %s", today, create)
        yyyy1 = int(today[0:4])
        mm1 = int(today[5:7])
        dd1 = int(today[8:10])
        cur_day = datetime.datetime(yyyy1, mm1, dd1)
        yyyy2 = int(create[0:4])
        mm2 = int(create[5:7])
        dd2 = int(create[8:10])
        cre_day = datetime.datetime(yyyy2, mm2, dd2)
        time_diff = relativedelta(cur_day, cre_day)
        days = time_diff.days
        return abs(days)


logging.info("Get user input")
# get user input
first_name = input("Enter First Name")
middle_name = input("Enter Middle Name")
last_name = input("Enter Last Name")
date_of_birth = input("Enter Date of Birth in format 'YYYY-MM-DD'")
gender = input("Enter Gender Male/Female")
nationality = input("Enter Nationality")
current_city = input("Enter Current City")
state = input("Enter State")
pin_code = input("Enter Pin-code")
qualification = input("Enter Qualification")
salary = input("Enter Salary")
pan = input("Enter PAN Number")
logging.info("Validating user input")
# validates input
REASON_VALIDATE = validate_name(first_name, last_name)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
REASON_VALIDATE = validate_dob(date_of_birth)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
REASON_VALIDATE = validate_gender(gender)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
REASON_VALIDATE = validate_nationality(nationality)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
REASON_VALIDATE = validate_current_city(current_city)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
REASON_VALIDATE = validate_state(state)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
REASON_VALIDATE = validate_qualification(qualification)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
REASON_VALIDATE = validate_pin_code(pin_code)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
REASON_VALIDATE = validate_salary(salary)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
REASON_VALIDATE = validate_pan(pan)
if REASON_VALIDATE != "SUCCESS":
    print_json_response("Validation failed", REASON_VALIDATE)
    sys.exit()
# generate current time
now = datetime.datetime.now()
current_time = now.strftime('%Y-%m-%d %H:%M:%S')
config_parser = configparser.RawConfigParser()
CONFIG_FILE_PATH = "config.txt"
config_parser.read(CONFIG_FILE_PATH)
hostname = config_parser.get('db-config', 'host')
username = config_parser.get('db-config', 'username')
pwd = config_parser.get('db-config', 'password')
db = config_parser.get('db-config', 'database')
logging.info("Create connection")
# get connection
connection = mysql.connector.connect(
    host=hostname,
    user=username,
    password=pwd,
    database=db
)
cursor = connection.cursor()
logging.info("Insert user input into request table")
# insert into db
SQL = "Insert into request(first_name, middle_name, last_name," \
      " date_of_birth, gender, nationality, current_city, state," \
      " pincode, qualification, salary, created_at, pan) values" \
      "( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
values = (first_name, middle_name, last_name, date_of_birth, gender,
          nationality, current_city, state, pin_code,
          qualification, salary, current_time, pan)
cursor.execute(SQL, values)
connection.commit()
# find request_id
SQL = "Select id from request where created_at = %s "
time = (current_time, )
cursor.execute(SQL, time)
myresult = cursor.fetchall()
request_id = myresult[0][0]
# find age
year = int(date_of_birth[0:4])
month = int(date_of_birth[5:7])
day = int(date_of_birth[8:10])
dob = datetime.datetime(year, month, day)
year1 = int(current_time[0:4])
month1 = int(current_time[5:7])
day1 = int(current_time[8:10])
current = datetime.datetime(year1, month1, day1)
time_difference = relativedelta(current, dob)
age = time_difference.years
logging.info("Check eligibility")
# check eligiblity
check = CheckEligibility(request_id, gender, age, nationality, state, pan, int(salary))
check.check_all(cursor, current_time)
json = check.create_json_object()
request = check.request_id
RESPONSE = check.response
REASON = check.reason
logging.info("Insert the response into response table")
# insert into db
SQL = "Insert into response(response, reason, request_id, json_object) values(%s,%s,%s,%s)"
values = (RESPONSE, REASON, request, json)
cursor.execute(SQL, values)
connection.commit()
print(json)
