import re


# Class for mixin email field
class EmailMixin:

    def __init__(self, string):
        if self.is_email(string):
            self.email = string
        else:
            raise TypeError("Invalid email")

    # Function for email validation
    def is_email(self, string):
        reg_exp = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        return True if re.search(reg_exp, string) else False


class Employee(EmailMixin):

    def __init__(self, name, email, salary_per_day):
        self.name = name
        super().__init__(email)
        try:
            self.salary_per_day = float(salary_per_day)
        except TypeError:
            print("Incorrect salary")

    def work(self):
       return "I come to the office."

    def check_salary(self, days):
        if not isinstance(days, int):
            raise TypeError('Invalid days param')
        return self.salary_per_day * days

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Programmer(Employee):

    def work(self):
        come = super().work()
        return come[:len(come) - 1] + " and start coding"


class Recruiter(Employee):

    def work(self):
        come = super().work()
        return come[:len(come) - 1] + " and start hiring"


class Candidate(EmailMixin):

    def __init__(self, full_name, email, technologies,
                 main_skill, main_skill_grade):
        self.full_name = full_name
        super().__init__(email)
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return self.full_name


class Vacancy(object):

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        return self.title
