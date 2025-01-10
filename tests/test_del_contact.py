import random
from model.contact import Contact

def test_del_first_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Test user for deletion"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.del_contact_by_id(contact.id)
    #assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)








