__author__ = "Alex"
from model.address import Address
from random import randrange

def test_delete_some_addrress(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    old_address = app.address.get_address_list()
    index = randrange(len(old_address))
    app.address.delete_address_by_index(index)
    new_address = app.address.get_address_list()
    assert len(old_address) - 1 == len(new_address)
    old_address[index:index + 1] = []
    assert old_address == new_address