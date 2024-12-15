from selenium.webdriver.support.expected_conditions import url_contains
from urllib3.util.url import url_attrs


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.get("http://localhost/addressbook/edit.php")

    def create_new(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.go_to_home_page_with_contacts_list()

    def count(self):
        wd = self.app.wd
        self.go_to_home_page_with_contacts_list()
        return len(wd.find_elements_by_name("selected[]"))

    def del_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.get("http://localhost/addressbook/delete.php?part=selected[];")
        wd.get("http://localhost/addressbook/index.php")

    def edit_first_contact(self, contact):
        wd = self.app.wd
        #open edit contact page
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit edit contact action
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        self.go_to_home_page_with_contacts_list()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("middlename", contact.middlename)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("title", contact.title)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.home)
        self.change_contact_field_value("mobile", contact.mobile)
        self.change_contact_field_value("work", contact.work)
        self.change_contact_field_value("fax", contact.fax)
        self.change_contact_field_value("email", contact.email)
        self.change_contact_field_value("email2", contact.email2)
        self.change_contact_field_value("email3", contact.email3)
        self.change_contact_field_value("homepage", contact.homepage)
        self.change_contact_field_value("bday", contact.bday)
        self.change_contact_field_value("bmonth", contact.bmonth)
        self.change_contact_field_value("byear", contact.byear)
        self.change_contact_field_value("aday", contact.aday)
        self.change_contact_field_value("amonth", contact.amonth)
        self.change_contact_field_value("ayear", contact.ayear)

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        Select = self.app.Select
        day_value = ['bday', 'bmonth', 'aday', 'amonth']
        if text is not None:
            if field_name not in day_value:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            else:
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def go_to_home_page_with_contacts_list(self):
        wd = self.app.wd
        # go to home page with list of contacts
        wd.find_element_by_link_text("home").click()
        wd.get("http://localhost/addressbook/index.php")
