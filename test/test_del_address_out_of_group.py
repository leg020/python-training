__author__ = 'Alex'
from model.group import Group
from model.address import Address
import random
import allure

def test_del_address_out_of_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_address_list()) == 0:
        app.address.create(Address(firstname='test'))
    if len(db.get_address_group_list()) == 0:
        address = random.choice(app.address.get_address_list())
        group = random.choice(app.group.get_group_list())
        app.address.selsect_address_by_id(address.id)
        app.group.select_group_into_address_list(group.id)
    with allure.step('Take info from db'):
        list = db.get_address_group_list()
    position = random.choice(list)
    with allure.step('Delete address %s from the group' % position):
        app.address.check_none_list(position.group_id)
    app.address.select_remove(position.id)
    with allure.step('Asserts'):
        new_list = db.get_address_group_list()
    new_list_address_in_group = app.address.check_none_list(position.group_id)
    for row in new_list_address_in_group:
        assert row.id is not position.id
    assert len(list) - 1 == len(new_list)
    list.remove(position)
    assert list == new_list

