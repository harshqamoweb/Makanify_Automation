from playwright.sync_api import expect

from pages.BasePage import BasePage

from utilities.random_data_generator import RandomDataGenerator
import time

class PropertiesPage(BasePage):

    btn_properties = "//button/span[contains(text(),'Properties')]"
    properties_heading = "//h1[contains(text(),'Individual Properties')]"
    btn_addProperty = "//button[contains(text(),'Add Property')]"
    heading_addProperty = "//h2[contains(text(),'Add New Property')]"
    dropdown_listingType = "//label[text()='Listing Type']/following::button[1]"
    dropdown_propertyCategory = "//span[contains(text(),'Select category')]"
    residential_category = "//span[contains(text(),'residential')]"
    dropdown_subCategory = "(//label[contains(.,'Sub Category')]/following::button[@role='combobox'])[1]"
    dropdown_selectProject = "//label[contains(.,'Project')]/following::button[@role='combobox'][1]"
    options_sub_category = "//label[@for='subcategory']/following-sibling::div//button"
    select_project_for_sell = "//div[contains(@data-value,'Rajhans Multiplex')]"
    select_project_for_rent = "//div[contains(@data-value,'Malbar Royal')]"
    select_state = "(//label[contains(.,'State')]/following::button[@role='combobox'])[1]"
    select_city = "(//label[contains(.,'City')]/following::button[@role='combobox'])[1]"
    select_area = "(//label[contains(.,'Locality/Area')]/following::button[@role='combobox'])[1]"
    select_configuration = "(//label[contains(.,'Configuration')]/following::button[@role='combobox'])[1]"
    select_furnishingType = "(//label[contains(.,'Furnishing')]/following::button[@role='combobox'])[1]"
    dropdown_options = "//div[@role='option']"
    input_carpetArea = "//input[contains(@id,'carpetArea')]"
    select_UOM = "(//label[contains(.,'UOM')]/following::button[@role='combobox'])[1]"
    input_ownerName = "//input[contains(@id,'ownerName')]"
    input_mobileNumber = "//input[contains(@id,'ownerContact')]"
    input_totalPrice = "//input[contains(@id,'price')]"
    dropdown_ownershipType = "(//button[contains(@role,'combobox')])[17]"
    input_monthly_rent = "//input[contains(@name,'monthlyRent')]"
    input_security_deposit = "//input[contains(@name,'securityDeposit')]"
    input_maintenance_charges = "//input[contains(@name,'maintenanceCharges')]"
    dropdown_brokerageAvailable = "//span[contains(text(),'Yes')]"
    select_brokerageAvailable = "//span[contains(text(),'No')]"
    input_brokerageAmount = "//input[contains(@name,'brokerageAmount')]"
    dropdown_availability = "(//label[contains(.,'Availability')]/following::button[@role='combobox'])[1]"
    input_PropertyTitle = "//input[contains(@placeholder,'3 BHK')]"
    input_PropertyDesc = "(//div[contains(@class,'border rounded-md')])[2]"
    btn_submit = "//button[contains(text(),'Submit')]"
    input_searchProperty = "//input[contains(@name,'searchQuery')]"

    def redirectToPropertiesTab(self):
        self.click(self.btn_properties)
        self.verify_visible(self.properties_heading)

    def addProperty(self, listing_type="Sell"):
        self.click(self.btn_addProperty)
        # time.sleep(1)
        self.verify_visible(self.heading_addProperty)
        # time.sleep(1)
        self.select_dropdown_by_text(self.dropdown_listingType,listing_type)
        self.waitForElementToBeVisible(self.dropdown_propertyCategory)
        self.click(self.dropdown_propertyCategory)
        self.waitForElementToBeVisible(self.residential_category)
        self.click(self.residential_category)
        self.select_random_dropdown_option(self.dropdown_subCategory,self.dropdown_options)
        # self.page.pause()
        # time.sleep(2)
        self.waitForElementToBeVisible(self.dropdown_selectProject)
        # self.waitForElementToBeEnabled(self.dropdown_selectProject)
        self.click(self.dropdown_selectProject)

        if listing_type.lower() == "sell":
            self.waitForElementToBeVisible(self.select_project_for_sell)
            self.click(self.select_project_for_sell)
        elif listing_type.lower() == "rent":
            self.waitForElementToBeVisible(self.select_project_for_rent)
            self.click(self.select_project_for_rent)

        get_selected_project_value = self.get_dropdown_selected_value(self.dropdown_selectProject)
        # print(f"Selected Project: {get_selected_project_value}")
        # self.page.pause()
        self.select_random_dropdown_option(self.select_state,self.dropdown_options)
        self.select_random_dropdown_option(self.select_city, self.dropdown_options)
        self.select_random_dropdown_option(self.select_area,self.dropdown_options)
        self.select_random_dropdown_option(self.select_configuration,self.dropdown_options)
        self.select_random_dropdown_option(self.select_furnishingType,self.dropdown_options)
        self.fill(self.input_carpetArea,RandomDataGenerator.random_carpet_area())
        # self.page.pause()
        self.select_random_dropdown_option(self.select_UOM,self.dropdown_options)
        # time.sleep(1)
        self.fill(self.input_ownerName,RandomDataGenerator.random_first_name())
        # time.sleep(1)
        self.fill(self.input_mobileNumber,RandomDataGenerator.random_indian_mobile())
        # time.sleep(1)
        if listing_type.lower() == "sell":
            self.fill(self.input_totalPrice, RandomDataGenerator.random_property_price())
            self.select_random_dropdown_option(self.dropdown_ownershipType, self.dropdown_options)

        elif listing_type.lower() == "rent":
            self.fill(self.input_monthly_rent, RandomDataGenerator.random_property_price())
            self.fill(self.input_security_deposit, RandomDataGenerator.random_property_price())
            self.fill(self.input_maintenance_charges, RandomDataGenerator.random_property_price())

        self.click(self.dropdown_brokerageAvailable)
        self.click(self.select_brokerageAvailable)
        self.waitForElementToBeInvisible(self.input_brokerageAmount)
        self.select_random_dropdown_option(self.dropdown_availability,self.dropdown_options)
        self.fill(self.input_PropertyTitle,RandomDataGenerator.random_property_title())
        generatedTitle = self.get_input_value(self.input_PropertyTitle)
        self.fill(self.input_PropertyDesc,RandomDataGenerator.random_property_description())
        self.click(self.btn_submit)
        self.verify_visible(self.input_searchProperty)
        self.fill(self.input_searchProperty,generatedTitle)
        self.page.wait_for_load_state("networkidle")
        # self.page.pause()
        # print(f"Generated Title: {generatedTitle}")
        expect(
            self.page.locator(f"text={generatedTitle}")
        ).to_be_visible(timeout=15000)
        return {
            "selected_project": get_selected_project_value
        }