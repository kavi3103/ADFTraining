from django.shortcuts import render
import datetime
import json
from dateutil.relativedelta import relativedelta
from .Check import CheckEligibility


def validate_name(first_name_input, last_name_input):
    """
        validates first name and last name
    """
    # logging.info("validating first name and last name")
    if len(first_name_input) == 0 or len(last_name_input) == 0:
        return "Invalid first name or last name"
    if not first_name_input.isalpha() or not last_name_input.isalpha():
        return "Invalid first name or last name"
    return "SUCCESS"


def validate_dob(dob_input):
    """
        validates date of birth
    """
    # logging.info("validating date of birth")
    try:
        datetime.datetime.strptime(dob_input, '%Y-%m-%d')
        return "SUCCESS"
    except ValueError:
        return "Invalid input for DOB"


def validate_gender(gender_input):
    """
        validates gender
    """
    # logging.info("validating gender")
    low_gender = gender_input.lower()
    if low_gender in ('male', 'female'):
        return "SUCCESS"
    return "Invalid input for gender"


def validate_nationality(nationality_input):
    """
        validates nationality
    """
    # logging.info("validating nationality")
    if len(nationality_input) == 0 or not nationality_input.isalpha():
        return "Invalid input for nationality"
    return "SUCCESS"


def validate_current_city(current_city_input):
    """
        validates city
    """
    # logging.info("validating city")
    if len(current_city_input) == 0 or not current_city_input.isalpha():
        return "Invalid input for current city"
    return "SUCCESS"


def validate_state(state_input):
    """
        validates state
    """
    # logging.info("validating state")
    if len(state_input) != 0 and all(char.isalpha() or char.isspace() for char in state_input):
        return "SUCCESS"
    return "Invalid input for state"


def validate_pin_code(pin_code_input):
    """
        validates pin-code
    """
    # logging.info("validating pin-code")
    if len(pin_code_input) == 6 and pin_code_input.isnumeric():
        return "SUCCESS"
    return "Invalid input for pin-code"


def validate_qualification(qualification_input):
    """
        validates qualification
    """
    # logging.info("validating qualification")
    if len(qualification_input) == 0 or not qualification_input.isalpha():
        return "Invalid input for qualification"
    return "SUCCESS"


def validate_salary(salary_input):
    """
            validates salary
    """
    # logging.info("validating salary")
    if len(salary_input) != 0 and salary_input.isnumeric() and int(salary_input) > 0:
        return "SUCCESS"
    return "Invalid input for salary"


def validate_pan(pan_input):
    """
            validates pan
    """
    if len(pan_input) == 10 and pan_input.isalnum():
        return "SUCCESS"
    return "Invalid input for pan"


def find_age(date_of_birth):
    now = datetime.datetime.now()
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')
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
    return age


def print_json_response(response, rea):
    """
    printing json object
    """
    dict_json = {"response": response, "reason": rea}
    json_obj = json.dumps(dict_json)
    # logging.info("Convert to json object")
    return json_obj


def validate_check_all(first, last, date_of_birth, gender, nationality, current_city, state, pin_code,
                       qualification, salary, pan):
    reason_validate = validate_name(first, last)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    reason_validate = validate_dob(date_of_birth)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    reason_validate = validate_gender(gender)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    reason_validate = validate_nationality(nationality)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    reason_validate = validate_current_city(current_city)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    reason_validate = validate_state(state)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    reason_validate = validate_qualification(qualification)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    reason_validate = validate_pin_code(pin_code)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    reason_validate = validate_salary(salary)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    reason_validate = validate_pan(pan)
    if reason_validate != "SUCCESS":
        json_ = print_json_response("Validation failed", reason_validate)
        return json_
    age = find_age(date_of_birth)
    check = CheckEligibility(gender, age, nationality, state, pan, int(salary))
    check.check_all()
    json_ = check.create_json_object()
    return json_


# Create your views here.
def home_view(request):
    return render(request, "home.html")


def next(request):
    first = request.POST['first_name']
    middle = request.POST['middle_name']
    last = request.POST['last_name']
    gender = request.POST['gender']
    dob = request.POST['dob']
    nationality = request.POST['nationality']
    city = request.POST['current_city']
    state = request.POST['state']
    pin = request.POST['pin_code']
    qualification = request.POST['qualification']
    salary = request.POST['salary']
    pan = request.POST['pan']
    json_obj = validate_check_all(first, last, dob, gender, nationality, city, state, pin, qualification, salary, pan)
    return render(request, "next.html", {'first': json_obj})
