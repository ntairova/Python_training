import allure

from model.contact import Contact

@allure.epic("Contact")
@allure.feature("Contact creation cases")
@allure.label("owner", "Nelya Tairova")
def test_add_new_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    with allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('When I add the contact %s to the list' % contact):
        app.contact.create_new(contact)
    with allure.step("Then the new contact list is equal to the old list with the added contact"):
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)








