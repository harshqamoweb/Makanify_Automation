from playwright.sync_api import expect, Page

from pages.BasePage import BasePage


class DashboardPage(BasePage):

    propertiesText = "//span[contains(text(),'Properties')]"
    heading_top_activities = "//h3[normalize-space()='Top Activities Today']"

    def verify_successful_login(self):
        self.verify_url("https://uat-makanify.workzy.co/dashboard")
        self.verify_visible(self.heading_top_activities)

    def clickOnPropertiesTab(self):
        self.click(self.propertiesText)