__author__ = "Alex"
from model.address import Address
from model.group import Group
import allure
import random

def test_add_address_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if len(app.address.check_none_list(value="[none]")) == 0:
        app.group.create(Group(name='test'))
        app.address.create(Address(firstname='test'))
    with allure.step('Take info from db'):
        old_list = db.get_address_group_list()
    address = random.choice(app.address.check_none_list(value="[none]"))
    group = random.choice(app.group.get_group_list())
    with allure.step('Paste address to the group'):
        old_address_list_in_group = app.address.check_none_list(value=group.id)
    for row in old_address_list_in_group:
        assert row.id is not address.id
    app.address.selsect_address_by_id(address.id)
    app.group.select_group_into_address_list(group.id)
    position = Address(id=address.id, group_id=group.id)
    with allure.step('Asserts'):
        new_list = db.get_address_group_list()
    new_address_list_in_group = app.address.check_none_list(value=group.id)
    old_address_list_in_group.append(address)
    assert old_address_list_in_group == new_address_list_in_group
    assert len(old_list) + 1 == len(new_list)
    old_list.append(position)
    assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)

"""""
    flag = False
    list_db = db.get_address_group_list()
    for row in list_db:
        if row.id == address.id and row.group_id == group.id:
            flag = True
    assert flag == True
"""