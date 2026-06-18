from pages.LeadsPage import LeadsPage
from pages.TasksPage import TasksPage
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage


def test_complete_task(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("testadminbroker@yopmail.com", "Test@123$")
    dashboardPage = DashboardPage(page)
    dashboardPage.verify_successful_login()
    leadsPage = LeadsPage(page)
    fetched_contact_name = leadsPage.add_lead_and_add_activities()
    taskPage = TasksPage(page)
    taskPage.complete_task(fetched_contact_name["customer_full_name"])