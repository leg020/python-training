# -*- coding: utf-8 -*-
from model.address import Address
import random
import string
import os.path
import json
import getopt
import sys
import jsonpickle



try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number of address', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/address.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a

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
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    out.write(jsonpickle.encode(testdata))