from pony.orm import *
from datetime import datetime
from model.group import Group
from model.address import Address
from pymysql.converters import decoders


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMAddress(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host,
                                database=name,
                                user=user,
                                password=password,
                                autocommit=True)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_address_to_model(self, addresses):
        def convert(address):
            return Address(id=str(address.id), firstname=address.firstname, lastname=address.lastname)
        return list(map(convert, addresses))


    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_address_list(self):
        return self.convert_address_to_model(select(c for c in ORMFixture.ORMAddress if c.deprecated is None))