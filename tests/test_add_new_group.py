from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    #print(old_groups)
    app.group.create(Group("test_group", "test_header", "test_footer"))
    new_groups = app.group.get_group_list()
    #print(old_groups)
    #print(new_groups)
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("", "", ""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)





