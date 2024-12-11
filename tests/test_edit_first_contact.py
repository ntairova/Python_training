from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact("edited_Nelya_test", "edited_middle_test", "edited_Tairova", "edited_NT", "edited_test_title", "edited_Starpoint",
                            "edited_home_address_for_testing 30-1-32", "1234567890", "9876543210", "123654987", "123",
                            "test1_edited@test.com", "test2_edited@test.com", "test3@test.com", "www.kvakva.com", "10", "March",
                            "1900", "1", "February", "2011", ''))
    app.session.logout()