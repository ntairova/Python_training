import getopt
import sys

import jsonpickle

from model.contact import Contact

import pytest
import random
import string
import random
import string
import os.path

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ string.punctuation + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone_string(maxlen):
    symbols = string.digits + " "*3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="",middlename= "", lastname="", nickname="", title="", company="", address="",
                     home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="")] + [
             Contact(firstname=random_string("firstname", 20),
                    middlename=random_string("middlename", 20),
                    lastname=random_string("lastname", 20),
                    nickname=random_string("nickname", 20),
                    title=random_string("title", 20),
                    company=random_string("company", 20),
                    address=random_string("address", 30),
                    home=random_phone_string(12),
                    mobile=random_phone_string(12),
                    work=random_phone_string(12),
                    fax=random_phone_string(12),
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
                    for i in range(n)
             ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
   # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write (jsonpickle.encode(testdata))