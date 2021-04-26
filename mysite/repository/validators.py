from mysite.mysite.settings import LAST_ELECTION_PERIOD


def permitted_age(age):
    if age >= LAST_ELECTION_PERIOD:
        return True
    return False
