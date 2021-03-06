__author__ = "Alex"
from model.address import Address
import random
import allure

def test_delete_some_addrress(app, db, check_ui):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    with allure.step('Take info from db'):
        old_address = db.get_address_list()
    address = random.choice(old_address)
    with allure.step('Delete %s from addressbook' % address):
        app.address.delete_address_by_id(address.id)
    with allure.step('Asserts'):
        new_address = db.get_address_list()
    assert len(old_address) - 1 == len(new_address)
    old_address.remove(address)
    assert old_address == new_address
    if check_ui:
        assert sorted(new_address, key=Address.id_or_max) == sorted(app.address.get_address_list(), key=Address.id_or_max)