from selenium.webdriver.support.ui import Select
__author__ = 'Alex'

class AddressHelper:

    def __init__(self, app):
        self.app = app

    def create(self, address):
        wd = self.app.wd
        # open page
        wd.find_element_by_link_text("add new").click()
        # fill address
        self.fill_address_form(address)
        # submit address
        wd.find_element_by_xpath("(//input[@name='submit'])").click()
        self.return_home()

    def fill_address_form(self, address):
        wd = self.app.wd
        self.change_field_value('firstname', address.firstname)
        self.change_field_value("middlename", address.middlename)
        self.change_field_value("lastname", address.lastname)
        self.change_field_value('nickname', address.nickname)
        # Вызывает исключение и тест падает причем даже если просто передавать ссылку
        # wd.find_element_by_name("photo").click()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys(address.photo)
        self.change_field_value('title', address.title)
        self.change_field_value('company', address.company)
        self.change_field_value('address', address.address_home)
        self.change_field_value('home', address.home)
        self.change_field_value('mobile', address.mobile)
        self.change_field_value('work', address.work)
        self.change_field_value('fax', address.work)
        self.change_field_value('email', address.email)
        self.change_field_value('email2', address.email2)
        self.change_field_value('email3', address.email3)
        self.change_field_value('homepage', address.homepage)
        #self.change_field_value('bday', address.bday)
        if address.bday is not None:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(address.bday)
            wd.find_element_by_name("bday").click()
        #self.change_field_value('bmonth',address.bmonth)
        if address.bmonth is not None:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(address.amonth)
            wd.find_element_by_name("bmonth").click()
        self.change_field_value('byear', address.byear)
        if address.aday is not None:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(address.aday)
            wd.find_element_by_name("aday").click()
        if address.amonth is not None:
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(address.amonth)
            wd.find_element_by_name("amonth").click()
        self.change_field_value('ayear', address.ayear)
        # wd.find_element_by_name("new_group").click()
        # wd.find_element_by_name("new_group").click()
        self.change_field_value('address2', address.address2)
        self.change_field_value('phone2', address.phone2)
        self.change_field_value('notes', address.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_address(self):
        wd = self.app.wd
        self.return_home()
        self.selsect_first_address()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_home()

    def selsect_first_address(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    """"
    def update_address(self, address):
        wd = self.app.wd
        self.return_home()
        wd.find_element_by_name("selected[]").click()
        # update address
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='import'])[1]/following::img[2]").click()
        # Edit info
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(address.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(address.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(address.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(address.nickname)
        # Вызывает исключение и тест падает причем даже если просто передавать ссылку
        # wd.find_element_by_name("photo").click()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys(address.photo)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(address.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(address.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address.address_home)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(address.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(address.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(address.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(address.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(address.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(address.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(address.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(address.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(address.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(address.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(address.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(address.aday)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(address.amonth)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(address.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(address.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(address.notes)
        # update info
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        self.return_home()
    """

    def modify_first_address(self, new_address_data):
        wd = self.app.wd
        self.return_home()
        self.selsect_first_address()
        # Open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill address form
        self.fill_address_form(new_address_data)
        # submit modification
        wd.find_element_by_xpath("(//input[@name='update'])").click()
        self.return_home()

    def return_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_home()
        return len(wd.find_elements_by_name("selected[]"))