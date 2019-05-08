__author__ = 'Alex'
from model.address import Address

def test_modify_address_firstname(app):
    if app.address.count() == 0:
        app.address.create(Address(lastname='test'))
    app.address.modify_first_address(Address(firstname="9999"))

def test_modify_address_middlename(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    app.address.modify_first_address(Address(lastname="9999"))