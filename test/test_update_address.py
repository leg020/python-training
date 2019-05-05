__author__ = 'Alex'
from model.address import Address

def test_update_group(app):
    app.session.login(username="admin", password="secret")
    app.address.update_address(Address(firstname="111", middlename="222", lastname="333", nickname="444",
                               photo="555", title="666", company="777",
                               address_home="888", home="999", mobile="1010", work="1100", fax="32", email="1123",
                               email2="44", email3="55", homepage="3", bday="-", bmonth="-",
                               byear="-", aday="-", amonth="-", ayear="-", address2="-", phone2="-",
                               notes="-"))
    app.session.logout()