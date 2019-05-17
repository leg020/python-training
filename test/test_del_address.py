__author__ = "Alex"
from model.address import Address

def test_delete_first_addrress(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    old_address = app.address.get_address_list()
    app.address.delete_first_address()
    new_address = app.address.get_address_list()
    assert len(old_address) - 1 == len(new_address)