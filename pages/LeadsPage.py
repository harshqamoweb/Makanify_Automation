from playwright.sync_api import expect
from datetime import datetime
from pages.BasePage import BasePage
from pages.ContactPage import ContactPage
from pages.PropertiesPage import PropertiesPage
import time, random

from pages.TasksPage import TasksPage
from utilities.random_data_generator import RandomDataGenerator


class LeadsPage(BasePage):

    btn_leads = "(//span[contains(text(),'Leads')])[1]"
    btn_add_lead = "//button[normalize-space()='Add Lead']"
    dropdown_select_contact = "//span[contains(text(),'Select contact')]"
    # dropdown_select_source = "//span[contains(text(),'Select source')]"
    verify_source = "//label[contains(.,'Source')]/following::button[@role='combobox'][1]"
    dropdown_options = "//div[@role='option']"
    verify_lead_stage = "(//button[contains(@role,'combobox')])[4]"
    dropdown_select_priority = "(//button[@role='combobox'])[5]"
    verify_assigned_to = "(//button[contains(@role,'combobox')])[6]"
    dropdown_buying_preference =  "(//button[@role='combobox'])[7]"
    select_buying_preference = "//div[@role='option'][contains(.,'Preferred Project')]"
    select_preference = "//div[contains(@data-value,'Preferred')]"
    label_project_name = " //label[@for='project']"
    select_project = "//span[contains(text(),'Select project')]"
    select_loan_required = "//label[normalize-space()='No']"
    dropdown_select_purpose = "//span[contains(text(),'Select purpose')]"
    btn_save_lead = "//button[normalize-space()='Save Lead']"
    input_search_leads = "//input[@placeholder='Search leads...']"
    verify_name_by_search =  "//div[@class='font-medium capitalize']"
    verify_project_by_search = "//div[@class='font-medium']"

    def redirect_to_leads_tab(self):
        self.click(self.btn_leads)
        self.verify_visible(self.btn_add_lead)

    def verify_project_exists(self, project_name):
        expect(
            self.page.locator(
                f"//div[@class='font-medium' and normalize-space()='{project_name}']"
            )
        ).to_be_visible()

    def add_lead(self):
        properties_page = PropertiesPage(self.page)
        properties_page.redirectToPropertiesTab()
        property_data = properties_page.addProperty()

        contact_page = ContactPage(self.page)
        contact_page.redirectToContactTab()
        contact_data = contact_page.add_contact()

        self.redirect_to_leads_tab()
        self.click(self.btn_add_lead)
        # time.sleep(2)
        # self.page.pause()
        # self.click(self.dropdown_select_contact)
        self.select_dropdown_by_text(self.dropdown_select_contact,contact_data["customer_full_name"])
        # self.waitForElementToBeVisible(self.verify_source)
        self.verify_dropdown_selected_value(self.verify_source, contact_data["source"])
        # self.select_random_dropdown_option(self.dropdown_select_source,self.dropdown_options)
        self.verify_dropdown_selected_value(self.verify_lead_stage, "New Lead")
        self.select_random_dropdown_option(self.dropdown_select_priority, self.dropdown_options)
        self.verify_dropdown_selected_value(self.verify_assigned_to, "testadmin broker")
        self.click(self.dropdown_buying_preference)
        self.click(self.select_buying_preference)
        # print(
        #     self.page.locator("//div[@role='option']").all_text_contents()
        # )
        # self.page.pause()
        # self.click(self.select_preference)
        # self.select_dropdown_by_text(self.dropdown_buying_preference, "Preferred project")
        self.verify_visible(self.label_project_name)
        # print(f"Project from Property Page: '{property_data['selected_project']}'")
        self.select_dropdown_by_text(self.select_project, property_data["selected_project"])
        self.click(self.select_loan_required)
        self.select_dropdown_by_text(self.dropdown_select_purpose, "Other")
        self.click(self.btn_save_lead)
        self.fill(self.input_search_leads, contact_data["first_name"])
        expect(
            self.page.locator(
                f"//div[text()='{contact_data['customer_full_name']}']"
            )
        ).to_be_visible()


    verify_lead_detail = "//div[@class='font-semibold leading-none tracking-tight']"
    btn_schedule = "//span[normalize-space()='Schedule']"
    verify_selected_activity = "//span[text()='Call Back']/parent::button"
    verify_activity_assigned_to = "(//button[contains(@role,'combobox')])[2]"
    verify_date = "(//button[@aria-haspopup='dialog'])[2]"
    select_time = "//span[contains(text(),'Select time')]"
    btn_submit_activity = "//button[@type='submit']"
    verify_call_activity = "//div[normalize-space()='schedule - call back']"
    verify_meeting_activity = "//div[normalize-space()='Meeting']"
    btn_meeting = "//span[normalize-space()='Meeting']"
    input_meeting_address = "//input[contains(@id,'address')]"
    input_comment_activities = "//textarea[contains(@id,'comment')]"

    def select_random_time_slot(self):
        self.page.wait_for_selector(
            "//button[.//span[contains(text(),'AM') or contains(text(),'PM')]]",
            timeout=10000
        )

        options = self.page.locator(
            "//button[not(@disabled)][.//span[contains(text(),'AM') or contains(text(),'PM')]]"
        )

        count = options.count()
        # print(f"Available slots: {count}")

        if count == 0:
            raise Exception("No enabled time slots found")

        random_option = options.nth(random.randint(0, count - 1))
        selected_time = random_option.inner_text().strip()

        random_option.click()

        return selected_time


    def add_lead_and_add_activities(self):
        today_date = datetime.now().strftime("%d %b %Y")

        contact_page = ContactPage(self.page)
        contact_page.redirectToContactTab()
        contact_data = contact_page.add_contact()

        self.redirect_to_leads_tab()
        self.click(self.btn_add_lead)
        self.select_dropdown_by_text(self.dropdown_select_contact, contact_data["customer_full_name"])
        self.verify_selected_value(self.verify_source, contact_data["source"])
        # self.page.pause()
        self.verify_dropdown_selected_value(self.verify_lead_stage, "New Lead")
        self.select_random_dropdown_option(self.dropdown_select_priority, self.dropdown_options)
        self.verify_dropdown_selected_value(self.verify_assigned_to, "testadmin broker")
        self.click(self.dropdown_buying_preference)
        self.click(self.select_buying_preference)
        self.verify_visible(self.label_project_name)
        self.select_dropdown_by_text(self.select_project, "Rajhans Multiplex - Surat, Gujarat")
        self.click(self.select_loan_required)
        self.select_dropdown_by_text(self.dropdown_select_purpose, "Other")
        self.click(self.btn_save_lead)
        self.fill(self.input_search_leads, contact_data["first_name"])
        expect(
            self.page.locator(
                f"//div[text()='{contact_data['customer_full_name']}']"
            )
        ).to_be_visible()
        self.click(f"//div[text()='{contact_data['customer_full_name']}']")
        self.verify_visible(self.verify_lead_detail)
        self.click(self.btn_schedule)
        # self.page.pause()
        self.verify_attribute(self.verify_selected_activity, "aria-selected", "true")
        self.verify_dropdown_selected_value(self.verify_activity_assigned_to, "testadmin broker")
        self.verify_text(self.verify_date,today_date)
        self.click(self.select_time)
        # self.page.pause()
        self.select_random_time_slot()
        self.click(self.btn_submit_activity)
        # self.page.pause()
        self.waitForElementToBeVisible(self.verify_call_activity)
        self.click(self.btn_schedule)
        self.click(self.btn_meeting)
        self.verify_dropdown_selected_value(self.verify_activity_assigned_to, "testadmin broker")
        self.verify_text(self.verify_date, today_date)
        self.click(self.select_time)
        self.select_random_time_slot()
        self.fill(self.input_meeting_address, RandomDataGenerator.random_address())
        self.fill(self.input_comment_activities, RandomDataGenerator.random_comment())
        self.click(self.btn_submit_activity)
        self.waitForElementToBeVisible(self.verify_meeting_activity)
        return {
            "customer_full_name": contact_data["customer_full_name"],
            "first_name": contact_data["first_name"]
        }

    btn_sell_property = "//span[contains(text(),'Sell / Rent Property')]"
    dropdown_select_project = "//button/span[contains(text(),'Select project')]"
    dropdown_select_property = "(//button[@role='combobox'])[3]"
    input_total_amount = "(//label[contains(.,'Total Amount')]/following::input[@id='totalAmount'])"
    input_amount_paid = "//input[contains(@id,'bookingAmount')]"
    input_rent_amount = "(//label[contains(.,'Rent Amount')]/following::input[@id='rentAmount'])"
    input_rent_amount_paid = "//input[contains(@id,'rentAmountPaid')]"
    input_deposit_amount = "(//label[contains(.,'Deposit Amount')]/following::input[@id='depositAmount'])"
    input_deposit_amount_paid = "//input[contains(@id,'depositAmountPaid')]"
    verify_sold_by = "(//button[@role='combobox'])[4]"
    verify_person_name = "(//label[contains(.,'Person 1 Name')]/following::input[@id='persons.0.name'])"
    input_comment = "//textarea[contains(@id,'comments')]"
    btn_confirm = "//button[contains(text(),'Confirm')]"
    btn_submit = "//button[contains(text(),'Submit')]"
    btn_explore_in_customer = "//button[contains(text(),'Explore in Customers')]"

    def sell_or_rent_property(self, property_name="Rajhans Multiplex - Surat, Gujarat"):
        contact_data = self.add_lead_and_add_activities()
        tasksPage = TasksPage(self.page)
        tasksPage.complete_task(contact_data["customer_full_name"])

        self.redirect_to_leads_tab()
        self.fill(self.input_search_leads, contact_data["first_name"])
        self.click(f"//div[text()='{contact_data['customer_full_name']}']")
        self.verify_visible(self.verify_lead_detail)
        self.click(self.btn_sell_property)

        if property_name.lower() == "rajhans multiplex - surat, gujarat":
            # print("1")
            # self.page.pause()
            self.select_dropdown_by_text(self.select_project, property_name)
            self.select_random_dropdown_option(self.dropdown_select_property, self.dropdown_options)
            total_amount = self.get_input_value(self.input_total_amount)
            self.fill(self.input_amount_paid, total_amount)
        elif property_name.lower() == "malbar royal - vadodara, gujarat":
            # print("2")
            # self.page.pause()
            self.select_dropdown_by_text(self.select_project, property_name)
            self.select_random_dropdown_option(self.dropdown_select_property, self.dropdown_options)
            total_rent_amount = self.get_input_value(self.input_rent_amount)
            self.fill(self.input_rent_amount_paid, total_rent_amount)
            total_deposit_amount = self.get_input_value(self.input_deposit_amount)
            self.fill(self.input_deposit_amount_paid, total_deposit_amount)

        self.verify_dropdown_selected_value(self.verify_sold_by, "testadmin broker")
        # self.page.pause()
        self.verify_input_value(self.verify_person_name, contact_data["customer_full_name"])
        self.fill(self.input_comment, RandomDataGenerator.random_comment())
        self.click(self.btn_confirm)
        self.click(self.btn_submit)
        self.waitForElementToBeVisible(self.btn_explore_in_customer)
        self.click(self.btn_explore_in_customer)
        return contact_data["customer_full_name"]