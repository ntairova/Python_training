from model.contact import Contact
from model.group import Group


def test_add_contact_in_group(app):
    if app.contact.count() == 0 and app.group.count() == 0:
        app.contact.create_new(Contact(firstname="Test user for deletion"))
        app.group.create(Group(name = 'Test_group'))