from model.group import Group


def test_add_group(app):
    app.group.create(Group("test_group", "test_header", "test_footer"))

def test_add_empty_group(app):
     app.group.create(Group("", "", ""))





