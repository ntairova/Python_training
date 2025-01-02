# -*- coding: utf-8 -*-
from sys import maxsize

from model.contact import Contact

import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10 #string.punctuation +
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Contact(firstname="",middlename= "", lastname="", nickname="", title="", company="", address="",
                     home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="")] + [
             Contact(firstname=random_string("firstname", 20),
                    middlename=random_string("middlename", 20),
                    lastname=random_string("lastname", 20),
                    nickname=random_string("nickname", 20),
                    title=random_string("title", 20),
                    company=random_string("company", 20),
                    address=random_string("address", 30),
                    home=random_string("home", 12),
                    mobile=random_string("mobile", 12),
                    work=random_string("work", 12),
                    fax=random_string("fax", 12),
                    email=random_string("email", 20),
                    email2=random_string("email2", 20),
                    email3=random_string("email3", 20),
                    homepage=random_string("homepage", 20))
                    #bday=random_string("bday", 2),
                   # bmonth=random_string("bminth", 20),
                    #byear=random_string("byear", 20),
                    #aday=random_string("aday", 20),
                   # amonth=random_string("amonth", 20),
                   # ayear=random_string("ayear", 20))
                    for i in range(5)
             ]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








