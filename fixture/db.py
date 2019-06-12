import pymysql.cursors
from model.group import Group
from model.address import Address

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          database=name,
                                          user=user,
                                          password=password,
                                          autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_address_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, middlename, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, last_name, middlename, nickname, company, title, address_home, home, mobile, work, fax, email, email2, email3, homepage, phone2) = row
                list.append(Address(lastname=last_name, firstname=first_name,
                                    middlename=middlename, nickname=nickname,
                                    company=company, title=title,
                                    address_home=address_home, id=str(id),
                                    home=home, mobile=mobile, work=work,
                                    fax=fax, email=email, email2=email2,
                                    email3=email3, homepage=homepage, phone2=phone2
                                    ))
        finally:
            cursor.close()
        return list

    def get_address_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(Address(id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()