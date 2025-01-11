import random
from model.group import Group


def test_edit_first_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name='Test_group'))
    old_groups = db.get_group_list()
    group = Group(name= "edited_test_name", header= "edited_test_header", footer ="edited_test_footer")
    group_to_edit = random.choice(old_groups)
    group.id = group_to_edit.id
    app.group.edit_group_by_id(group_to_edit.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(group_to_edit)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



