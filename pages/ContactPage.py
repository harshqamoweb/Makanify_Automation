from playwright.sync_api import expect

from pages.BasePage import BasePage
from utilities.random_data_generator import RandomDataGenerator
import time


class ContactPage(BasePage):

    btn_contacts = "//span[contains(text(),'Contacts')]"
    btn_add_contact = "//span[contains(text(),'Add Contact')]"
    heading_add_contact_form = "//h2[contains(text(),'Add New Contact')]"
    input_first_name = "//input[contains(@name,'firstName')]"
    input_last_name = "//input[contains(@name,'lastName')]"
    dropdown_select_source = "//label[contains(.,'Source')]/following::button[@role='combobox'][1]"
    dropdown_options = "//div[@role='option']"
    input_phone_number = "//input[contains(@id,'phone.0')]"
    verify_country = "(//button[contains(@role,'combobox')])[4]"
    # state_clear_btn = "(//button[@role='combobox']/following-sibling::button)[2]"
    dropdown_state = "//label[contains(.,'State')]/following::button[@role='combobox'][1]"
    # city_clear_btn = "(//button[@role='combobox']/following-sibling::button)[3]"
    dropdown_city = "//label[contains(.,'City')]/following::button[@role='combobox'][1]"
    input_pincode = "//input[contains(@id,'pinCode')]"
    btn_save_contact = "//button[@type='button'][normalize-space()='Save Contact']"
    input_search = "//input[contains(@placeholder,'Search contacts')]"
    # dynamic path = // span[contains(text(), 'akshay kumar')]
    # dynamic path = // td[contains(text(), '+91 8356588569')]

    def redirectToContactTab(self):
        self.click(self.btn_contacts)
        self.verify_url("https://uat-makanify.workzy.co/contacts")

    def add_contact(self):

        first_name = RandomDataGenerator.random_first_name()
        last_name = RandomDataGenerator.random_last_name()
        pincode = RandomDataGenerator.random_pincode()

        self.click(self.btn_add_contact)
        self.verify_visible(self.heading_add_contact_form)
        # time.sleep(1)
        self.fill(self.input_first_name,first_name)
        # time.sleep(1)
        self.fill(self.input_last_name,last_name)
        # time.sleep(1)
        # full_name = f"{first_name} {last_name}"
        # self.page.pause()
        self.select_random_dropdown_option(self.dropdown_select_source,self.dropdown_options)
        # print(self.page.locator(self.dropdown_select_source).inner_text())
        selected_source = self.get_dropdown_selected_value(self.dropdown_select_source)
        # time.sleep(1)
        self.fill(self.input_phone_number,RandomDataGenerator.random_indian_mobile())
        self.verify_dropdown_selected_value(self.verify_country,"india")
        # self.page.pause()
        # self.waitForElementToBeVisible(self.dropdown_state)
        # self.click(self.state_clear_btn)
        self.select_random_dropdown_option(self.dropdown_state, self.dropdown_options)
        # expect(self.page.locator(self.dropdown_options).first).to_be_visible()
        # self.waitForElementToBeVisible(self.dropdown_city)
        # self.click(self.city_clear_btn)
        self.select_random_dropdown_option(self.dropdown_city, self.dropdown_options)
        # self.page.pause()
        self.fill(self.input_pincode,"")
        # time.sleep(1)
        # self.page.pause()
        self.fill(self.input_pincode,pincode)
        # actual_value = self.page.locator(self.input_pincode).input_value()
        # print(f"Generated: {pincode}")
        # print(f"In Field : {actual_value}")
        self.click(self.btn_save_contact)
        # self.page.pause()
        self.verify_visible(self.input_search)
        self.fill(self.input_search,first_name)
        expect(self.page.locator(f"//span[contains(text(), '{first_name}')]")).to_be_visible()
        return {
            "first_name": first_name,
            "last_name": last_name,
            "customer_full_name": f"{first_name} {last_name}",
            "source": selected_source
        }