import pytest
import time

from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage

# @pytest.mark.smoke
def test_positive_login_test(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("testadminbroker@yopmail.com","Test@123$")
    # time.sleep(10)
    dashboardPage = DashboardPage(page)
    dashboardPage.verify_successful_login()

# def test_incorrect_username_test(page):
#     loginPage = LoginPage(page)
#     loginPage.navigateToWebsite()
#     loginPage.login("admin@yahoo.com","Admin123!")
#     loginPage.verifyToastMessage("No account with this email has been registered.")
#
# def test_incorrectPasswordTest(page):
#     loginPage = LoginPage(page)
#     loginPage.navigateToWebsite()
#     loginPage.login("admin@gmail.com","Admin123@")
#     loginPage.verifyToastMessage("Invalid credentials.")
#
# def test_blankFieldValidation(page):
#     loginPage = LoginPage(page)
#     loginPage.navigateToWebsite()
#     loginPage.blankFieldValidation()