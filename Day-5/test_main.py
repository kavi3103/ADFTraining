import pytest
import main
from main import CheckEligibility


class TestValidation:

    @pytest.mark.parametrize("first, last, expected", [("", "s", "Invalid first name or last name"),
                                                       ("kavi", "", "Invalid first name or last name"),
                                                       ("", "", "Invalid first name or last name"),
                                                       ("876fresef", "kav", "Invalid first name or last name"),
                                                       ("kavi", "v.#@", "Invalid first name or last name"),
                                                       ("Kavitha", "S", "SUCCESS")])
    def test_validate_name(self, first, last, expected):
        result = main.validate_name(first, last)
        assert result == expected

    @pytest.mark.parametrize("dob_input,expected", [("78-hyg-327", "Invalid input for DOB"),
                                                    ("22-03-2000", "Invalid input for DOB"),
                                                    ("2000-04-01", "SUCCESS")])
    def test_validate_dob(self, dob_input, expected):
        result = main.validate_dob(dob_input)
        assert result == expected

    @pytest.mark.parametrize("gender_input, expected", [("Male", "SUCCESS"), ("female", "SUCCESS"),
                                                        ("hjgje", "Invalid input for gender")])
    def test_validate_gender(self, gender_input, expected):
        result = main.validate_gender(gender_input)
        assert result == expected

    @pytest.mark.parametrize("nationality_input, expected", [("", "Invalid input for nationality"),
                                                             ("uh843dc", "Invalid input for nationality"),
                                                             ("Indian", "SUCCESS")])
    def test_validate_nationality(self, nationality_input, expected):
        result = main.validate_nationality(nationality_input)
        assert result == expected

    @pytest.mark.parametrize("current_city_input, expected", [("", "Invalid input for current city"),
                                                              ("uh843dc", "Invalid input for current city"),
                                                              ("Chennai", "SUCCESS")])
    def test_validate_current_city(self, current_city_input, expected):
        result = main.validate_current_city(current_city_input)
        assert result == expected

    @pytest.mark.parametrize("state_input, expected", [("", "Invalid input for state"),
                                                       ("uh843dc", "Invalid input for state"),
                                                       ("tamil nadu", "SUCCESS")])
    def test_validate_state(self, state_input, expected):
        result = main.validate_state(state_input)
        assert result == expected

    @pytest.mark.parametrize("qualification_input, expected", [("", "Invalid input for qualification"),
                                                               ("uh843dc", "Invalid input for qualification"),
                                                               ("degree", "SUCCESS")])
    def test_validate_qualification(self, qualification_input, expected):
        result = main.validate_qualification(qualification_input)
        assert result == expected

    @pytest.mark.parametrize("pin_code_input, expected", [("7565", "Invalid input for pin-code"),
                                                          ("ujntgd", "Invalid input for pin-code"),
                                                          ("600082", "SUCCESS")])
    def test_validate_pin_code(self, pin_code_input, expected):
        result = main.validate_pin_code(pin_code_input)
        assert result == expected

    @pytest.mark.parametrize("salary_input, expected", [("", "Invalid input for salary"),
                                                        ("ujntgd", "Invalid input for salary"),
                                                        ("0", "Invalid input for salary"),
                                                        ("65978", "SUCCESS")])
    def test_validate_salary(self, salary_input, expected):
        result = main.validate_salary(salary_input)
        assert result == expected

    @pytest.mark.parametrize("pan_input, expected", [("7565%49870", "Invalid input for pan"),
                                                     ("7565", "Invalid input for pan"),
                                                     ("600082kghi", "SUCCESS")])
    def test_validate_pan(self, pan_input, expected):
        result = main.validate_pan(pan_input)
        assert result == expected

    @pytest.mark.parametrize("gender, age, expected_response, expected_reason",
                             [('male', 18, "FAILED", "Age does not meet eligibility criteria"),
                              ('female', 18, "FAILED", "Age does not meet eligibility criteria"),
                              ('male', 22, "SUCCESS", "")])
    def test_check_age(self, gender, age, expected_response, expected_reason):
        c = CheckEligibility(1, gender, age, '', '', '', 0)
        c.check_age()
        assert c.response == expected_response
        assert c.reason == expected_reason

    @pytest.mark.parametrize("nationality, expected_response, expected_reason", [
        ("Chinese", "FAILED", "Nationality should be Indian or American"), ("INDIAN", "SUCCESS", "")])
    def test_check_nationality(self, nationality, expected_response, expected_reason):
        c = CheckEligibility(1, '', 0, nationality, '', '', 0)
        c.check_nationality()
        assert c.response == expected_response
        assert c.reason == expected_reason

    @pytest.mark.parametrize("state,  expected_response, expected_reason", [
        ("kerala", "FAILED", "State does not meet eligibility criteria"), ("TAmil nadu", "SUCCESS", "")])
    def test_check_state(self, state,  expected_response, expected_reason):
        c = CheckEligibility(1, '', 0, '', state, '', 0)
        c.check_state()
        assert c.response == expected_response
        assert c.reason == expected_reason

    @pytest.mark.parametrize("salary, expected_response, expected_reason", [
        (5000, "FAILED", "Salary does not meet eligibility criteria"),
        (100000, "FAILED", "Salary does not meet eligibility criteria"),
        (40000, "SUCCESS", "")])
    def test_check_salary(self, salary, expected_response, expected_reason):
        c = CheckEligibility(1, '', 0, '', '', '', salary)
        c.check_salary()
        assert c.response == expected_response
        assert c.reason == expected_reason

