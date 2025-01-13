from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
from timeit import timeit


#def test_group_list(app, db):
    #ui_list = app.group.get_group_list()
  #  print(timeit(lambda: app.group.get_group_list(), number=1))
  #  def clean(group):
  #      return Group(id=group.id, name=group.name.strip())
    #db_list = map(clean, db.get_group_list())
  #  print(timeit(lambda: map(clean, db.get_group_list()), number=10))
   # assert False#sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

#def test_contact_list(app, db):
    #ui_list = app.contact.get_contact_list()
    #print(timeit(lambda: app.group.get_group_list(), number=1))
    #db_list = db.get_contact_list()
    #print("qwe", db_list)
    #print("asd", ui_list)
    #print(timeit(lambda: map(clean, db.get_group_list()), number=10))
    #assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)







