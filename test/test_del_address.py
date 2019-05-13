__author__ = "Alex"
from model.address import Address

def test_delete_first_addrress(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    app.address.delete_first_address()