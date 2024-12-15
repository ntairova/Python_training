from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = 'Test_group'))
    app.group.edit_first_group(Group("edited_group_name", "edited_test_header", "edited_test_footer"))

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = 'Test_group'))
    app.group.edit_first_group(Group(name="group_name_updated"))