# -*- coding: utf-8 -*-
from sys import maxsize

from model.contact import Contact

def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("Nelya", "middle_test", "Tairova", "NT", "test_title", "Starpoint",
                            "home_address_for_testing 30-1-32", "1234567890", "9876543210", "123654987", "123",
                            "test1@test.com", "test2@test.com", "test3@test.com", "www.kvakva.com", "1", "February",
                            "1900", "1", "February", "2001", "")
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








