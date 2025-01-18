from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_in_group(app):
    if app.contact.count() == 0 and app.group.count() == 0:
        app.contact.create_new(Contact(firstname="Test user"))
        app.group.create(Group(name = 'Test_group'))
    elif app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Test user"))
    elif app.group.count() == 0:
        app.group.create(Group(name='Test_group'))
    groups = db.get_group_list()
    group = random.choice(groups)
    print(group)
    old_contacts_in_group = db.get_contacts_in_group(group)
    contacts = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_in_group(group.id, contact.id)
    new_contacts_in_group = db.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)








