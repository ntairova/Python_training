import random

import allure

from model.contact import Contact

@allure.epic("Contact")
@allure.feature("Contact deletion cases")
@allure.label("owner", "Nelya Tairova")
def test_del_first_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create_new(Contact(firstname="Test user for deletion"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When I delete the contact % s from the list' % contact):
        app.contact.del_contact_by_id(contact.id)
    with allure.step('Then the contact list is equal to the old list without deleted contact'):
        #assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)








