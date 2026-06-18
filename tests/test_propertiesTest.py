from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.PropertiesPage import PropertiesPage
import time, pytest

# @pytest.mark.parametrize("i", range(10))
@pytest.mark.order(2)
def test_addProperty(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("testadminbroker@yopmail.com", "Test@123$")
    # time.sleep(10)
    dashboardPage = DashboardPage(page)
    dashboardPage.verify_successful_login()
    propertiesPage = PropertiesPage(page)
    propertiesPage.redirectToPropertiesTab()
    propertiesPage.addProperty(listing_type="Rent")