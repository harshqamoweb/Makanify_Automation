from pages.CustomerPage import CustomerPage
from pages.LeadsPage import LeadsPage
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
import time


def test_add_lead(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("testadminbroker@yopmail.com", "Test@123$")
    # time.sleep(10)
    dashboardPage = DashboardPage(page)
    dashboardPage.verify_successful_login()
    leadsPage = LeadsPage(page)
    leadsPage.add_lead()

def test_add_lead_and_add_activities(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("testadminbroker@yopmail.com", "Test@123$")
    dashboardPage = DashboardPage(page)
    dashboardPage.verify_successful_login()
    leadsPage = LeadsPage(page)
    leadsPage.add_lead_and_add_activities()

def test_sell_or_rent_property(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("testadminbroker@yopmail.com", "Test@123$")
    dashboardPage = DashboardPage(page)
    dashboardPage.verify_successful_login()
    leadsPage = LeadsPage(page)
    contact_data = leadsPage.sell_or_rent_property(property_name="Malbar Royal - Vadodara, Gujarat")
    customerPage = CustomerPage(page)
    customerPage.verify_customer_page()
    customerPage.verify_customer_after_sell_property(contact_data)