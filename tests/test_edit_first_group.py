import random

import allure

from model.group import Group

@allure.epic("Group")
@allure.feature("Modification cases")
@allure.label("owner", "Nelya Tairova")
def test_edit_random_group(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if app.group.count() == 0:
            app.group.create(Group(name='Test_group'))
        old_groups = db.get_group_list()
        group = Group(name= "edited_test_name", header= "edited_test_header", footer ="edited_test_footer")
    with allure.step('Given a random group from the list'):
        group_to_edit = random.choice(old_groups)
        group.id = group_to_edit.id
    with allure.step('When I modify the group_name for group % s to group_name = % s from the list' % (group_to_edit, group.name)):
        app.group.edit_group_by_id(group_to_edit.id, group)
    with allure.step('Then the new group list is equal to the old group list'):
        new_groups = db.get_group_list()
        old_groups.remove(group_to_edit)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



