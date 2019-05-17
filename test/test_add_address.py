# -*- coding: utf-8 -*-
from model.address import Address

def test_new_address(app):
    old_address = app.address.get_address_list()
    app.address.create(Address(firstname="dsf", middlename="dcsc", lastname="cdsc", nickname="sdcs", photo="C:\\fakepath\\title.gif", title="rdewd", company="sdassdasa",
                               address_home="cdss", home="scac", mobile="sacas", work="asxsax", fax="sxsa", email="sxcsa", email2="sac", email3="sc", homepage="sc", bday="15", bmonth="September",
                               byear="1994", aday="12", amonth="May", ayear="2020", address2="xxxx", phone2="xsw", notes="wece"))
    new_address = app.address.get_address_list()
    assert len(old_address) + 1 == len(new_address)

def test_new_empty_address(app):
    old_address = app.address.get_address_list()
    app.address.create(Address(firstname="", middlename="", lastname="", nickname="",
                               photo="", title="", company="",
                               address_home="", home="", mobile="", work="", fax="", email="",
                               email2="", email3="", homepage="", bday="", bmonth="-",
                               byear="", aday="", amonth="-", ayear="", address2="", phone2="",
                               notes=""))
    new_address = app.address.get_address_list()
    assert len(old_address) + 1 == len(new_address)