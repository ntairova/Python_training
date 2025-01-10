#from selenium.webdriver.support.expected_conditions import url_contains
#from urllib3.util.url import url_attrs
import re


from model.contact import Contact



class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

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
        self.contact_cache = None

    def del_contact_by_id(self, id):
        wd = self.app.wd
        # select first contact
        self.go_to_home_page_with_contacts_list()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.go_to_home_page_with_contacts_list()
        self.open_contact_to_edit_by_index(index)
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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id = '%s']" % id).click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page_with_contacts_list()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                   all_phones_from_home_page = all_phones, address=address,
                                                  all_emails_from_home_page = all_emails))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page_with_contacts_list()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=home, mobile=mobile, work=work, address=address,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
         wd = self.app.wd
         self.open_contact_view_by_index(index)
         text = wd.find_element_by_id("content").text
         home = re.search("H: (.*)", text).group(1)
         mobile = re.search("M: (.*)", text).group(1)
         work = re.search("W: (.*)", text).group(1)
         return Contact(home=home, mobile=mobile, work=work)





