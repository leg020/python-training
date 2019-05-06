__author__ = 'Alex'
from model.address import Address

def test_modify_address_firstname(app):
    app.address.modify_first_address(Address(firstname="9999"))

def test_modify_address_middlename(app):
    app.address.modify_first_address(Address(lastname="9999"))