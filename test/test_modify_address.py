__author__ = 'Alex'
from model.address import Address

def test_modify_address_firstname(app):
    if app.address.count() == 0:
        app.address.create(Address(lastname='test'))
    old_address = app.address.get_address_list()
    address = Address(firstname="9999")
    address.id = old_address[0].id
    address.lastname = old_address[0].lastname
    app.address.modify_first_address(address)
    new_address = app.address.get_address_list()
    assert len(old_address) == len(new_address)
    old_address[0] = address
    assert sorted(old_address, key=Address.id_or_max) == sorted(new_address, key=Address.id_or_max)

def test_modify_address_middlename(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    old_address = app.address.get_address_list()
    app.address.modify_first_address(Address(lastname="9999"))
    new_address = app.address.get_address_list()
    assert len(old_address) == len(new_address)