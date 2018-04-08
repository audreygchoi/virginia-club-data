A_UNKNOWN_MEMBERSHIP = "Unknown"
A_NONMENBER_MEMBERSHIP = "Non-Member"
A_SOCIAL_MEMBERSHIP = "Social Member"
A_CLUBHOUSE_MEMBERSHIP = "Clubhose Member"

class Member:
    def __init__(self, name):
        self.name = name
        self.membership_type = 0

    @property
    def first_name(self):
        return self.first_name

    @property
    def last_name(self):
        return self.last_name

    @property
    def email(self):
        return self.email

    @property
    def membership_type(self):
        return self.get_membership_type

    def get_full_membership_type(self):
        if membership_type == 1:
            return A_NONMENBER_MEMBERSHIP
        elif membership_type == 2:
            return A_SOCIAL_MEMBERSHIP
        elif membership_type == 4:
            return A_CLUBHOUSE_MEMBERSHIP
        else:
            return A_UNKNOWN_MEMBERSHIP
