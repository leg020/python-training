__author__ = 'Alex'
import re
from model.address import Address

def test_phones_on_home_page(app, db):
    contact_list = sorted(app.address.get_address_list(), key=Address.id_or_max)
    contact_list_from_db = sorted(db.get_address_list(), key=Address.id_or_max)
    for contact in contact_list:
        index = contact_list.index(contact)
        assert contact.lastname == contact_list_from_db[index].lastname
        assert contact.firstname == contact_list_from_db[index].firstname
        assert contact.address_home == contact_list_from_db[index].address_home
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contact_list_from_db[index])
        assert contact.all_mail_from_home_page == merge_mail_like_on_home_page(contact_list_from_db[index])

def test_phones_on_contact_view_page(app, db):
    contact_list_from_db = sorted(db.get_address_list(), key=Address.id_or_max)
    for contact in contact_list_from_db:
        contact_from_view_page = app.address.get_contact_from_view_page_by_id(contact.id)
        assert contact_from_view_page.home == contact.home
        assert contact_from_view_page.work == contact.work
        assert contact_from_view_page.mobile == contact.mobile
        assert contact_from_view_page.phone2 == contact.phone2

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_mail_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))