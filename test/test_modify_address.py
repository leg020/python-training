__author__ = 'Alex'
from model.address import Address

def test_modify_address_firstname(app):
    app.session.login(username="admin", password="secret")
    app.address.modify_first_address(Address(firstname="9999"))
    app.session.logout()

def test_modify_address_middlename(app):
    app.session.login(username="admin", password="secret")
    app.address.modify_first_address(Address(lastname="9999"))
    app.session.logout()