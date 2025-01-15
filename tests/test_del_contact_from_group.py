from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_contact_from_group(app):
    if app.contact.count() == 0 and app.group.count() == 0:
        app.contact.create_new(Contact(firstname="Test user"))
        app.group.create(Group(name = 'Test_group'))
    elif app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Test user"))
    elif app.group.count() == 0:
        app.group.create(Group(name='Test_group'))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_contacts_in_group(group)) == 0:
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_in_group(group.id, contact.id)
    old_contacts_not_in_group = db.get_contacts_not_in_group(group)
    old_contacts_in_group = db.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group(group.id, contact.id)
    new_contacts_in_group = db.get_contacts_in_group(group)
    new_contacts_not_in_group = db.get_contacts_not_in_group(group)
    old_contacts_not_in_group.append(contact)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_not_in_group, key=Contact.id_or_max) == sorted(new_contacts_not_in_group, key=Contact.id_or_max)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)


