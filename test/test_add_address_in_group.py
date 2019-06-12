__author__ = "Alex"
from model.address import Address
from model.group import Group
import random

def test_add_address_in_group(app, db):
    if len(app.address.check_none_list()) == 0:
        app.group.create(Group(name='test'))
        app.address.create(Address(firstname='test'))
    address = random.choice(app.address.check_none_list())
    group = random.choice(app.group.get_group_list())
    app.address.selsect_address_by_id(address.id)
    app.group.select_group_into_address_list(group.id)
    flag = False
    list_db = db.get_address_group_list()
    for row in list_db:
        if row.id == address.id and row.group_id == group.id:
            flag = True
    assert flag == True