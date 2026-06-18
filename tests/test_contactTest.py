from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.ContactPage import ContactPage
import time, pytest


@pytest.mark.order(3)
def test_addContact(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("testadminbroker@yopmail.com", "Test@123$")
    # time.sleep(10)
    dashboardPage = DashboardPage(page)
    dashboardPage.verify_successful_login()
    contactPage = ContactPage(page)
    contactPage.redirectToContactTab()
    contactPage.add_contact()