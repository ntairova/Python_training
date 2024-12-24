#from selenium.webdriver.support.expected_conditions import url_contains
#from urllib3.util.url import url_attrs
from selenium.webdriver.common.by import By

from model.contact import Contact


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
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.go_to_home_page_with_contacts_list()
        return len(wd.find_elements_by_name("selected[]"))

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact
        self.go_to_home_page_with_contacts_list()
        self.select_contact(index)
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.get("http://localhost/addressbook/delete.php?part=selected[];")
        wd.get("http://localhost/addressbook/index.php")
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.go_to_home_page_with_contacts_list()
        #open edit contact page
        self.select_contact(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit edit contact action
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        self.go_to_home_page_with_contacts_list()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]")[0].click()

    def select_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

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
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("Delete")) > 0:
            return
        # go to home page with list of contacts
        wd.find_element_by_link_text("home").click()

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page_with_contacts_list()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_elements_by_css_selector("td")[1].text
                firstname = element.find_elements_by_css_selector("td")[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache .append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache )


