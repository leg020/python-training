# -*- coding: utf-8 -*-
from model.address import Address



def test_new_address(app, json_address):
    address = json_address
    old_address = app.address.get_address_list()
    app.address.create(address)
    assert len(old_address) + 1 == app.address.count()
    new_address = app.address.get_address_list()
    old_address.append(address)
    assert sorted(old_address, key=Address.id_or_max) == sorted(new_address, key=Address.id_or_max)

