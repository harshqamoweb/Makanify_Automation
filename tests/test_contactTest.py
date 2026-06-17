from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.ContactPage import ContactPage
import time


def test_addContact(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("sales@moweb.com", "Test@321")
    # time.sleep(10)
    dashboardPage = DashboardPage(page)
    dashboardPage.verify_successful_login()
    contactPage = ContactPage(page)
    contactPage.redirectToContactTab()
    contactPage.add_contact()