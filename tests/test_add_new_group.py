import allure
import allure_pytest

from model.group import Group

#@allure.epic("Creation cases")
def test_add_group(app, db, json_groups, check_ui):
     group = json_groups
     #with allure.step('a group list'):
     old_groups = db.get_group_list()
     #with allure.step('add the group to the list'):
     app.group.create(group)
     assert len(old_groups) + 1 == app.group.count()
     new_groups = db.get_group_list()
     old_groups.append(group)
     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
     if check_ui:
         assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)





