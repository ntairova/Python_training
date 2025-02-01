import random
import allure
from model.contact import Contact

@allure.epic("Contact")
@allure.feature("Contact modification cases")
@allure.label("owner", "Nelya Tairova")
def test_edit_first_contact(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if app.contact.count() == 0:
            app.contact.create_new(Contact(firstname="Nelya"))
        old_contacts = db.get_contact_list()
        contact = Contact("333Edited_Nelya_test", "edited_middle_test", "edited_Tairova", "edited_NT", "edited_test_title", "edited_Starpoint",
                                 "edited_home_address_for_testing 30-1-32", "1234567890", "9876543210", "123654987", "123",
                                 "test1_edited@test.com", "test2_edited@test.com", "test3@test.com", "www.kvakva.com", "10", "March",
                                 "1900", "1", "February", "2011", '')
    with allure.step('Given a random contact from the list'):
        contact_to_edit = random.choice(old_contacts)
        contact.id = contact_to_edit.id
    with allure.step('When I modify the contact % s from tha list. Change first/lastnames for firstname= % s and lastname= % s' % (
        contact_to_edit, contact.firstname, contact.lastname)):
        app.contact.edit_contact_by_id(contact_to_edit.id, contact)
    with allure.step('Then the new contact list is equal to the old contact list'):
        old_contacts.remove(contact_to_edit)
        old_contacts.append(contact)
        assert len(old_contacts) == app.contact.count()
        new_contacts = db.get_contact_list()
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



#
# def test_edit_first_contact_firstname_email_birthdate(app):
#     if app.contact.count() == 0:
#         app.contact.create_new(Contact(firstname="Nelya"))
#     app.contact.edit_first_contact(Contact(firstname="Nelya_Update", email="test@test.com", bday= "20"))