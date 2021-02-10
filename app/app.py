import models
from random import choice
from string import ascii_lowercase, digits
import logging
import datetime


logging.basicConfig(filename='logs.txt', filemode='a',
                    format='%(asctime)s - %(message)s', datefmt="%d-%b-%y: %H:%M:%S")
letters = ascii_lowercase + digits


def generate_email():
    chars = [choice(letters) for _i in range(10)]
    return "".join(chars) + "@yak.com"


def main():
    # Creating Programmer instances
    coder = models.Programmer("Yak", generate_email(), 67)
    print(coder.work())
    print(coder.check_salary(10))
    coder2 = models.Programmer("Yak1", generate_email(), 66)
    print(f"{coder}, {coder2}")

    # Creating Recruiter instance
    recruiter = models.Recruiter("Jak", generate_email(), 58)
    print(recruiter.work())
    print(recruiter.check_salary(10))
    print(f"{recruiter}")

    # Creating candidates instances
    candidate1 = models.Candidate("candidate1", generate_email(), "technologies", "skill", 2)
    candidate2 = models.Candidate("candidate2", generate_email(), "technologies", "skill", 2)
    candidate3 = models.Candidate("candidate3", generate_email(), "technologies", "skill", 2)
    print(f"{candidate1}, {candidate2}, {candidate3}")

    # Creating vacancy instances
    vacancy1 = models.Vacancy("title", "skill", 2)
    vacancy2 = models.Vacancy("title2", "skill", 2)
    print(f"{vacancy1}, {vacancy2}")

    # Checking email validation
    try:
        inv_email = models.Programmer("", "invalid_email", 56)
    except TypeError as e:
        logging.exception(e)
    else:
        print("email validation don't work")

    # Checking email uniquity
    try:
        with open("emails.txt", "r") as f:
            inv_email = f.readline()
        inv_entity = models.Programmer("", inv_email[:len(inv_email) - 1], 78)
    except ValueError as e:
        logging.exception(e)
    else:
        print("Two identical emails exists!!!")

    # Checking work exception
    try:
        candidate1.work()
    except models.UnableToWorkException as e:
        logging.exception(e)


if __name__ == "__main__":
    main()
