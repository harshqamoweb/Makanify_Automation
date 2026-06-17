from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage


def test_checkToggleBtn(page):
    loginPage = LoginPage(page)
    dashboard = DashboardPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com","Admin123!")
    dashboard.verify_successful_login()

def test_clickProfileBtnToVerifyRole(page):
    loginPage = LoginPage(page)
    dashboardPage = DashboardPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com", "Admin123!")
    dashboardPage.verifyTextAfterLogin()
    dashboardPage.clickProfileBtnAndConfirmRole()

def test_verifySearchFunctionalityOnSidebar(page):
    loginPage = LoginPage(page)
    dashboardPage = DashboardPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com", "Admin123!")
    dashboardPage.verifyTextAfterLogin()
    dashboardPage.searchFunctionalityOnSideBar()

def test_searchingDepartmentUsingLocationFilter(page):
    loginPage = LoginPage(page)
    dashboardPage = DashboardPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com", "Admin123!")
    dashboardPage.verifyTextAfterLogin()
    dashboardPage.searchingDepartmentUsingLocationFilter()

def test_updateStatusOfDepartmentFromActiveToInactiveAndVerifyBySearch(page):
    loginPage = LoginPage(page)
    dashboardPage = DashboardPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com", "Admin123!")
    dashboardPage.verifyTextAfterLogin()
    dashboardPage.updateStatusOfDepartmentFromActiveToInactiveAndVerifyBySearch()

def test_redirectToDepartmentByClickingHomeBtn(page):
    loginPage = LoginPage(page)
    dashboardPage = DashboardPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com", "Admin123!")
    dashboardPage.verifyTextAfterLogin()
    dashboardPage.redirectToDepartmentByClickingHomeBtn()