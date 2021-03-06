__author__ = "Alex"
from sys import maxsize


class Address:

    def __init__(self, firstname=None, middlename=None, lastname=None,
                        nickname=None, photo=None, title=None,
                        company=None, address_home=None, home=None,
                        mobile=None, work=None, fax=None, email=None,
                        email2=None, email3=None, homepage=None,
                        bday=None, bmonth=None, byear=None, aday=None,
                        amonth=None, ayear=None, address2=None,
                        phone2=None, notes=None, id=None, group_id=None,
                        all_phones_from_home_page=None, all_mail_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address_home = address_home
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.group_id = group_id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mail_from_home_page = all_mail_from_home_page

    def __repr__(self):
        return "%s: %s; %s; %s; %s; %s; %s" % (self.id, self.lastname, self.firstname, self.home, self.email, self.aday, self.ayear)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize