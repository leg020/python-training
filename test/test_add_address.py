# -*- coding: utf-8 -*-
from model.address import Address
import allure



def test_new_address(app, db, json_address, check_ui):
    address = json_address
    with allure.step('Take address from db'):
        old_address = db.get_address_list()
    with allure.step('Create address %s' % address):
        app.address.create(address)
    with allure.step('Append address and use assert'):
        new_address = db.get_address_list()
    old_address.append(address)
    assert sorted(old_address, key=Address.id_or_max) == sorted(new_address, key=Address.id_or_max)
    if check_ui:
        assert sorted(new_address, key=Address.id_or_max) == sorted(app.address.get_address_list(),
                                                                    key=Address.id_or_max)
