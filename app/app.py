import models


def main():
    # Creating Programmer instances
    coder = models.Programmer("Yak", "yak@yak.com", 67)
    print(coder.work())
    print(coder.check_salary(10))
    coder2 = models.Programmer("Yak1", "yak@yak.com", 66)
    print(f"{coder}, {coder2}")

    # Creating Recruiter instance
    recruiter = models.Recruiter("Jak", "jak@jak.com", 58)
    print(recruiter.work())
    print(recruiter.check_salary(10))
    print(f"{recruiter}")

    # Creating candidates instances
    candidate1 = models.Candidate("candidate1", "yak@yak.com", "technologies", "skill", 2)
    candidate2 = models.Candidate("candidate2", "yak@yak.com", "technologies", "skill", 2)
    candidate3 = models.Candidate("candidate3", "yak@yak.com", "technologies", "skill", 2)
    print(f"{candidate1}, {candidate2}, {candidate3}")

    # Creating vacancy instances
    vacancy1 = models.Vacancy("title", "skill", 2)
    vacancy2 = models.Vacancy("title2", "skill", 2)
    print(f"{vacancy1}, {vacancy2}")

    # Checking email validation
    try:
        inv_email = models.Programmer("", "invalid_email", 56)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
