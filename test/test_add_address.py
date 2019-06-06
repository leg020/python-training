# -*- coding: utf-8 -*-
from model.address import Address



def test_new_address(app, db, json_address):
    address = json_address
    old_address = db.get_address_list()
    app.address.create(address)
    new_address = db.get_address_list()
    old_address.append(address)
    assert sorted(old_address, key=Address.id_or_max) == sorted(new_address, key=Address.id_or_max)

