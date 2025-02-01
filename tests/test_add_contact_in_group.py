import allure

from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

#db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
@allure.epic("Contacts and groups relation")
@allure.feature("Contact added into the group")
@allure.label("owner", "Nelya Tairova")
def test_add_contact_in_group(app, db):
    with allure.step("Precondition"):
        if app.contact.count() == 0 and app.group.count() == 0:
            app.contact.create_new(Contact(firstname="Test user"))
            app.group.create(Group(name = 'Test_group'))
        elif app.contact.count() == 0:
            app.contact.create_new(Contact(firstname="Test user"))
        elif app.group.count() == 0:
            app.group.create(Group(name='Test_group'))
        groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(groups)
        old_contacts_in_group = db.get_contacts_in_group(group) # получаю список контактов выбранной группы
        if len(db.get_contacts_not_in_group(group)) == 0: #проверяю наличие контаков вне выбранной группы, если таких нет,
            # создаю новый контакт
            app.contact.create_new(Contact(firstname="Test user"))
    with allure.step('Given a random contact not in selected group %s' %group):
        contacts = db.get_contacts_not_in_group(group)
        contact = random.choice(contacts)
    with allure.step('When a random contact: % s is added in selected group %s' % (contact, group)):
        app.contact.add_contact_in_group(group.id, contact.id)
    with allure.step("Then contacts in new group list is equal to the old list with the added contact"):
        new_contacts_in_group = db.get_contacts_in_group(group)
        old_contacts_in_group.append(contact)
        assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    #
    #






