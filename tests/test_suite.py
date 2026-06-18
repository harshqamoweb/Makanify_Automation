from test_loginTest import test_positive_login_test
from test_contactTest import test_addContact
from test_leadsTest import test_add_lead, test_add_lead_and_add_activities, test_sell_or_rent_property
from test_tasksTest import test_complete_task
from test_propertiesTest import test_addProperty

class TestSuite:

    def test_suite(self, page):
        test_positive_login_test(page)
        test_addProperty(page)
        test_addContact(page)
        test_add_lead(page)
        test_add_lead_and_add_activities(page)
        test_complete_task(page)
        test_sell_or_rent_property(page)