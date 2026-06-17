from playwright.sync_api import expect
from pages.BasePage import BasePage


class CustomerPage(BasePage):

    heading_customers = "//h1[contains(text(),'Customers')]"
    input_search_customers = "//input[contains(@placeholder,'Search customers...')]"

    def verify_customer_page(self):
        self.waitForElementToBeVisible(self.heading_customers)

    def verify_customer_after_sell_property(self, customer_name):
        self.verify_customer_page()
        self.fill(self.input_search_customers, customer_name)
        expect(
                self.page.locator(
                    f"//div[text()='{customer_name}']"
                )
            ).to_be_visible()