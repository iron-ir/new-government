LAST_ELECTION_PERIOD = '1400:03:28'


def permitted_age(age):
    if age >= LAST_ELECTION_PERIOD:
        return True
    return False
