from model.contact import Contact

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Test user for deletion"))
    app.contact.del_first_contact()








