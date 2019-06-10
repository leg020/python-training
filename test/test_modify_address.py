__author__ = 'Alex'
from model.address import Address
import random

def test_modify_address_firstname(app, db, check_ui):
    if app.address.count() == 0:
        app.address.create(Address(lastname='test'))
    old_address = db.get_address_list()
    text = "8999"
    address = random.choice(old_address)
    index = old_address.index(address)
    address.firstname = text
    app.address.modify_address_by_id(address.id, address)
    new_address = db.get_address_list()
    assert len(old_address) == len(new_address)
    old_address[index] = address
    assert sorted(old_address, key=Address.id_or_max) == sorted(new_address, key=Address.id_or_max)
    if check_ui:
        assert sorted(new_address, key=Address.id_or_max) == sorted(app.address.get_address_list(), key=Address.id_or_max)

def test_modify_address_middlename(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    old_address = app.address.get_address_list()
    app.address.modify_first_address(Address(lastname="9999"))
    new_address = app.address.get_address_list()
    assert len(old_address) == len(new_address)