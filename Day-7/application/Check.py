import datetime
import json
from django.db import connection
from dateutil.relativedelta import relativedelta
import logging

logging.basicConfig(filename='Info.log',level=logging.INFO)


class CheckEligibility:
    """
        checks eligibility criteria
    """

    def __init__(self, request_id, gender_input, age_input,
                 nationality_input, state_input, pan_input, salary_input):
        self.request_id = request_id
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
        dict_obj = {"request_id":self.request_id,"response": self.response}
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

    def check_pan(self, today):
        """
            check whether request is recieved in last 5 days
        """
        logging.info("checking whether request is recieved in last 5 days")
        with connection.cursor() as dbcursor:
            query = "SELECT created_at FROM application_request where created_at != %s and pan = %s"
            value = [today, self.pan]
            dbcursor.execute(query, value)
            rows = dbcursor.fetchall()
            for row, value in enumerate(rows):
                logging.info("checking %s row from result in checking that request is recieved in last 5 days", row)
                create = value[0]
                days = self.find_difference(today, str(create))
                if days <= 5:
                    self.reason = "Recently request received in last 5 days"
                    self.response = "FAILED"
                    break

    def check_all(self, today):
        """
            call all methods
        """
        self.check_salary()
        self.check_pan(today)
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
