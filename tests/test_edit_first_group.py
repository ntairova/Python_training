import random
from model.group import Group


def test_edit_first_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name='Test_group'))
    old_groups = db.get_group_list()
    group = Group("edited_group_name", "edited_test_header", "edited_test_footer")
    group_to_edit = random.choice(old_groups)
    app.group.edit_group_by_id(group_to_edit.id, group)
    new_groups = db.get_group_list()
    for i in old_groups:
        if i.id == group_to_edit.id:
            i.name = group.name
            i.header = group.header
            i.footer = group.footer
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



