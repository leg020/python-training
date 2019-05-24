# -*- coding: utf-8 -*-
from model.address import Address
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Address(firstname="",
                    middlename="",
                    lastname="",
                    nickname="",
                    photo="",
                    title="",
                    company="",
                    address_home="",
                    home="",
                    mobile="",
                    work="",
                    fax="",
                    email="",
                    email2="",
                    email3="",
                    homepage="",
                    bday="",
                    bmonth="-",
                    byear="",
                    aday="",
                    amonth="-",
                    ayear="",
                    address2="",
                    phone2="",
                    notes="")] + \
           [Address(firstname=random_string("firstname", 10),
                    middlename=random_string('middlename', 10),
                    lastname=random_string('lastname', 10),
                    nickname=random_string('nickname', 10),
                    photo="C:\\fakepath\\title.gif",
                    title=random_string('title', 10),
                    company=random_string('company', 10),
                    address_home=random_string('address_home', 10),
                    home=random_string('8', 10),
                    mobile=random_string('8', 10),
                    work=random_string('8', 10),
                    fax=random_string('8', 10),
                    email=random_string('8', 10),
                    email2=random_string('8', 10),
                    email3=random_string('8', 10),
                    homepage=random_string('8', 10),
                    bday=str(random.randrange(1, 32)),
                    bmonth="September",
                    byear=random_string('8', 10),
                    aday=str(random.randrange(1, 32)),
                    amonth="May",
                    ayear=random_string('8', 10),
                    address2=random_string('8', 10),
                    phone2=random_string('8', 10),
                    notes=random_string('8', 10))
    for i in range(5)]

@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_new_address(app, address):
    old_address = app.address.get_address_list()
    app.address.create(address)
    assert len(old_address) + 1 == app.address.count()
    new_address = app.address.get_address_list()
    old_address.append(address)
    assert sorted(old_address, key=Address.id_or_max) == sorted(new_address, key=Address.id_or_max)

