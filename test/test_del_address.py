__author__ = "Alex"
from model.address import Address
import random

def test_delete_some_addrress(app, db):
    if app.address.count() == 0:
        app.address.create(Address(firstname='test'))
    old_address = db.get_address_list()
    address = random.choice(old_address)
    app.address.delete_address_by_id(address.id)
    new_address = db.get_address_list()
    assert len(old_address) - 1 == len(new_address)
    old_address.remove(address)
    assert old_address == new_address