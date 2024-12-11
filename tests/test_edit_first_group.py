from model.group import Group


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("edited_group_name", "edited_test_header", "edited_test_footer"))
    app.session.logout()