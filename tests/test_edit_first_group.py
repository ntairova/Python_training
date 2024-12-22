from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = 'Test_group'))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group("edited_group_name", "edited_test_header", "edited_test_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = 'Test_group'))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="group_name_updated"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)