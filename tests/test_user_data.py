
from random import randrange
import re

import allure

from model.contact import Contact

@allure.epic("Contact")
@allure.feature("Contact's phones and emails data cases")
@allure.label("owner", "Nelya Tairova")
def test_user_data_on_home_page(app, db):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create_new(Contact(firstname="Nelya"))
    with allure.step("Contact's emails and phones on homepage are equal to data in database"):
        contacts_from_home_page = app.contact.get_contact_list()
        contacts_from_db = db.get_contact_list()
        for row, row_db in zip(sorted(contacts_from_home_page, key=Contact.id_or_max), sorted(contacts_from_db, key=Contact.id_or_max)):
            assert row.firstname == row_db.firstname
            assert row.lastname == row_db.lastname
            assert row.address == row_db.address
            assert row.all_emails_from_home_page == merge_emails_like_on_home_page(row_db)
            assert row.all_phones_from_home_page == merge_phones_like_on_home_page(row_db)

def clear(s):
    return re.sub("[- ()]", "" , s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                      map(lambda x: clear(x),
                         filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))



