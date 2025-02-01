import random

import allure

from model.group import Group

@allure.epic("Group")
@allure.feature("Deletion cases")
@allure.label("owner", "Nelya Tairova")
def test_delete_some_group(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name = 'Test_group'))
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I delete the group % s from the list' % group):
        app.group.delete_group_by_id(group.id)
        #assert len(old_groups) - 1 == app.group.count()
    with allure.step('Then the new group list is equal to the old list without deleted group'):
        new_groups = db.get_group_list()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


