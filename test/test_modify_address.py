__author__ = 'Alex'
from model.address import Address
from random import randrange

def test_modify_address_firstname(app):
    if app.address.count() == 0:
        app.address.create(Address(lastname='test'))
    old_address = app.address.get_address_list()
    index = randrange(len(old_address))
    address = Address(firstname="9999")
    address.id = old_address[index].id
    address.lastname = old_address[index].lastname
    app.address.modify_address_by_index(index, address)
    new_address = app.address.get_address_list()
    assert len(old_address) == len(new_address)
    old_address[index] = address
    assert sorted(old_address, key=Address.id_or_max) == sorted(new_address, key=Address.id_or_max)

def test_modify_address_middlename(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    old_address = app.address.get_address_list()
    app.address.modify_first_address(Address(lastname="9999"))
    new_address = app.address.get_address_list()
    assert len(old_address) == len(new_address)