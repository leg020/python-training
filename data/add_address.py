from model.address import Address
import random
import string


constant = [
    Address(firstname="firstname1",
            middlename="middlename1",
            lastname="lastname1",
            nickname="nickname1",
            photo="C:\\fakepath\\title.gif",
            title="title1",
            company="company1",
            address_home="address_home1",
            home="home1",
            mobile="mobile1",
            work="work1",
            fax="fax1",
            email="email1",
            email2="email2",
            email3="email3",
            homepage="homepage1",
            bday="1",
            bmonth="-",
            byear="2000",
            aday="2",
            amonth="-",
            ayear="2000",
            address2="address21",
            phone2="phone21",
            notes="notes1"),
    Address(firstname="firstname2",
            middlename="middlename2",
            lastname="lastname2",
            nickname="nickname2",
            photo="C:\\fakepath\\title.gif",
            title="title2",
            company="company2",
            address_home="address_home2",
            home="home2",
            mobile="mobile2",
            work="work2",
            fax="fax2",
            email="email2",
            email2="email22",
            email3="email23",
            homepage="homepage2",
            bday="2",
            bmonth="September",
            byear="2002",
            aday="23",
            amonth="May",
            ayear="2002",
            address2="address22",
            phone2="phone22",
            notes="notes2")
]

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