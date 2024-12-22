from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = 'Test_group'))
    old_groups = app.group.get_group_list()
    group = Group("edited_group_name", "edited_test_header", "edited_test_footer")
    group.id=old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    print(old_groups[0])
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name = 'Test_group'))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="group_name_updated"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)