__author__ = 'Alex'
from model.address import Address

def test_modify_address_firstname(app):
    if app.address.count() == 0:
        app.address.create(Address(lastname='test'))
    old_address = app.address.get_address_list()
    app.address.modify_first_address(Address(firstname="9999"))
    new_address = app.address.get_address_list()
    assert len(old_address) == len(new_address)

def test_modify_address_middlename(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    old_address = app.address.get_address_list()
    app.address.modify_first_address(Address(lastname="9999"))
    new_address = app.address.get_address_list()
    assert len(old_address) == len(new_address)