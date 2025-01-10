import random
from model.group import Group


def test_edit_first_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name = 'Test_group'))
    old_groups = db.get_group_list()
    group_data = Group("edited_group_name1", "edited_test_header1", "edited_test_footer1")
    #index = randrange(len(old_contacts))
   # contact.id = old_contacts[index].id
    #app.contact.edit_contact_by_index(index, contact)
    group= random.choice(old_groups)
    print(group)
    app.group.edit_group_by_id(group.id, group_data)
    #assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    print(group)
    for index, item in enumerate(old_groups):
        if item == group:
            print('da!!!!')
            old_groups[index] = group_data
    print(new_groups)
    print(old_groups)

    #old_groups[index] = group
   # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
   # if check_ui:
       # assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_edit_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name = 'Test_group'))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="group_name_updated"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)