from playwright.sync_api import expect, Page, Locator
import random


class BasePage:
    websiteUrl = "https://uat-makanify.workzy.co/"
    # toastMessage = "//p[contains(@class,'MuiTypography-body1 css-1cp532n')]"

    def __init__(self, page: Page):
        self.page = page

    def navigateToWebsite(self):
        self.page.goto(self.websiteUrl)

    def click(self, locator):
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        element.click()

    def dblClick(self,locator):
        self.page.locator(locator).dblclick()

    def click_by_text(self,text):
        self.page.get_by_text(text).click()

    def dblclick_by_text(self,text):
        self.page.get_by_text(text).dblclick()

    def fill(self, locator, text):
        self.page.locator(locator).fill(str(text))

    def waitForElementToBeVisible(self, locator,timeout=10000):
        expect(self.page.locator(locator)).to_be_visible(timeout=timeout)

    def waitForElementToBeEnabled(self, locator,timeout=15000):
        expect(self.page.locator(locator)).to_be_enabled(timeout=timeout)

    def waitForElementToBeInvisible(self, locator):
        expect(self.page.locator(locator)).to_be_hidden()

    # def verifyToastMessage(self, text):
    #     expect(self.page.locator(self.toastMessage)).to_contain_text(text)

    def verify_visible(self,locator):
        expect(self.page.locator(locator)).to_be_visible()

    # def verify_invisible(self,locator):
    #     expect(self.page.locator(locator)).to_be_invisible()

    def to_have_value(self,locator,text:str):
        expect(self.page.locator(locator)).to_have_value(text)

    def verify_text(self,locator,text):
        expect(self.page.locator(locator)).to_contain_text(text)

    def press_key(self,locator,key):
        self.page.locator(locator).press(key)

    def verify_url(self,expectedUrl,timeout=30000):
        expect(self.page).to_have_url(expectedUrl,timeout=timeout)

    def scroll_to_element(self, locator):
        self.page.locator(locator).scroll_into_view_if_needed()

    # def select_random_dropdown_option(self, dropdown_locator, options_locator):
    #     self.page.locator(dropdown_locator).click()
    #
    #     expect(
    #         self.page.locator(options_locator).first
    #     ).to_be_visible(timeout=10000)
    #
    #     options = self.page.locator(options_locator)
    #     count = options.count()
    #
    #     random_index = random.randint(0, count - 1)
    #
    #     options.nth(random_index).click()

    def wait_for_text(self, locator):
        expect(self.page.locator(locator)).not_to_have_text("", timeout=30000)

    def wait_for_textarea_value(self, locator):
        expect(self.page.locator(locator)).not_to_have_text("", timeout=30000)

    def get_input_value(self, locator):
        return self.page.locator(locator).input_value()

    def verify_dropdown_selected_value(self, locator, expected_value):
        expect(self.page.locator(locator)).to_contain_text(expected_value)

    def verify_input_value(self, locator, expected_value):
        expect(self.page.locator(locator)).to_have_value(expected_value)

    def select_dropdown_by_text(self, dropdown_locator, value:str):
        self.click(dropdown_locator)
        option = self.page.get_by_role("option", name=value)
        option.wait_for()
        option.click()

    def get_dropdown_selected_value(self, locator):
        return self.page.locator(locator).inner_text().strip()

    def wait_for_dropdown_options(self, options_locator, timeout=15000):
        expect(
            self.page.locator(options_locator).first
        ).to_be_visible(timeout=timeout)

    def select_random_dropdown_option(
            self,
            dropdown_locator,
            options_locator
    ):
        self.waitForElementToBeVisible(dropdown_locator)

        dropdown = self.page.locator(dropdown_locator)

        # Current selected value (works for most combo boxes)
        current_value = (
            dropdown.locator("span").first.inner_text().strip().lower()
        )

        dropdown.click()

        self.page.wait_for_timeout(1000)

        options = self.page.locator(options_locator)

        expect(options.first).to_be_visible(timeout=5000)

        count = options.count()

        if count == 0:
            raise Exception("No options found in dropdown")

        # Collect options except current selection
        valid_options = []

        for i in range(count):
            option = options.nth(i)
            option_text = option.inner_text().strip()

            if option_text.lower() != current_value:
                valid_options.append(option)

        if not valid_options:
            raise Exception("No alternative options available")

        selected_option = random.choice(valid_options)

        selected_text = selected_option.inner_text().strip()

        selected_option.click()

        self.page.wait_for_timeout(500)

        return selected_text

    def verify_attribute(self, locator: str, attribute: str, value: str):
        expect(
            self.page.locator(locator)
        ).to_have_attribute(attribute, value)

    def press_escape(self):
        self.page.keyboard.press("Escape")