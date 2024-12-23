from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Nelya"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact("Edited_Nelya_test", "edited_middle_test", "edited_Tairova", "edited_NT", "edited_test_title", "edited_Starpoint",
                             "edited_home_address_for_testing 30-1-32", "1234567890", "9876543210", "123654987", "123",
                             "test1_edited@test.com", "test2_edited@test.com", "test3@test.com", "www.kvakva.com", "10", "March",
                             "1900", "1", "February", "2011", '')
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#
# def test_edit_first_contact_firstname_email_birthdate(app):
#     if app.contact.count() == 0:
#         app.contact.create_new(Contact(firstname="Nelya"))
#     app.contact.edit_first_contact(Contact(firstname="Nelya_Update", email="test@test.com", bday= "20"))