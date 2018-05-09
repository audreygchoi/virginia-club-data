# id SERIAL PRIMARY KEY,
# first_name varchar(30),
# last_name varchar(30),
# membership_type integer);

from django.db import models

class Member(models.model):
    class Meta:
        db_table = 'memberships'
        app_label = 'data'

    TYPE_MEMBERSHIP_UNKNOWN = 0
    TYPE_MEMBERSHIP_NONMEMBER = 1
    TYPE_MEMBERSHIP_SOCIAL = 2
    TYPE_MEMBERSHIP_CLUBHOUSE = 3

    ENUM_MEMBERSHIP_UKNOWN = 'MEMBERSHIP_UNKNOWN'
    ENUM_MEMBERSHIP_NONMENBER = 'MEMBERSHIP_NONMEMBER'
    ENUM_MEMBERSHIP_SOCIAL = 'MEMBERSHIP_SOCIAL'
    ENUM_MEMBERHSIP_CLUBHOUSE = 'MEMBERSHIP_CLUBHOUSE'

    MEMBERSHIP_TYPES = {
        TYPE_MEMBERSHIP_UNKNOWN: "Unknown"
        TYPE_MEMBERSHIP_NONMEMBER: "Non-Member"
        TYPE_MEMBERSHIP_SOCIAL: "Social Member"
        TYPE_MEMBERSHIP_CLUBHOUSE: "Clubhose Member"
    }

    MEMBERSHIP_TYPE_TO_ENUM = {
        TYPE_MEMBERSHIP_UNKNOWN: ENUM_MEMBERSHIP_UKNOWN
        TYPE_MEMBERSHIP_NONMEMBER: ENUM_MEMBERSHIP_NONMENBER
        TYPE_MEMBERSHIP_SOCIAL: ENUM_MEMBERSHIP_SOCIAL
        TYPE_MEMBERSHIP_CLUBHOUSE: ENUM_MEMBERHSIP_CLUBHOUSE
    }

    MEMBERSHIP_ENUM_TO_TYPE = {
        ENUM_MEMBERSHIP_UKNOWN: TYPE_MEMBERSHIP_UNKNOWN
        ENUM_MEMBERSHIP_NONMENBER: TYPE_MEMBERSHIP_NONMEMBER
        ENUM_MEMBERSHIP_SOCIAL: TYPE_MEMBERSHIP_SOCIAL
        ENUM_MEMBERHSIP_CLUBHOUSE: TYPE_MEMBERSHIP_CLUBHOUSE
    }

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

    # def get_full_membership_type(self):
    #     if membership_type == 1:
    #         return A_NONMENBER_MEMBERSHIP
    #     elif membership_type == 2:
    #         return A_SOCIAL_MEMBERSHIP
    #     elif membership_type == 4:
    #         return A_CLUBHOUSE_MEMBERSHIP
    #     else:
    #         return A_UNKNOWN_MEMBERSHIP
