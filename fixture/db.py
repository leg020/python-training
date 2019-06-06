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
            cursor.execute("select id, firstname, lastname, address from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, last_name, address_home) = row
                list.append(Address(lastname=last_name, firstname=first_name,
                                    address_home=address_home, id=str(id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()