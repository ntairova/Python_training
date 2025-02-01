from random import randrange
import re
import allure


@allure.epic("Contact")
@allure.feature("Contact's phone data cases")
@allure.label("owner", "Nelya Tairova")
def test_phones_on_home_page(app):
    contacts = app.contact.get_contact_list()
    with allure.step('Given a random contact from the list'):
        index = randrange(len(contacts))
    with allure.step("Contact phones on homepage are equal to contact phones on edit page"):
        contact_from_home_page = app.contact.get_contact_list()[index]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

@allure.epic("Contact")
@allure.feature("Contact's phone data cases")
@allure.label("owner", "Nelya Tairova")
def test_phones_on_contact_view_page(app):
    contacts = app.contact.get_contact_list()
    with allure.step('Given a random contact from the list'):
        index = randrange(len(contacts))
    with allure.step("Contact phones on contact view page are equal to contact phones on contact edit page"):
        contact_from_view_page = app.contact.get_contact_from_view_page(index)
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        assert contact_from_view_page.home == contact_from_edit_page.home
        assert contact_from_view_page.work == contact_from_edit_page.work
        assert contact_from_view_page.mobile == contact_from_edit_page.mobile


def clear(s):
    return re.sub("[- ()]", "" , s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work]))))


