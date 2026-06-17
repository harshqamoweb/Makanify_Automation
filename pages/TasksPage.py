from pages.BasePage import BasePage
# from pages.LeadsPage import LeadsPage
from utilities.random_data_generator import RandomDataGenerator


class TasksPage(BasePage):


    btn_tasks_tab = "//span[contains(text(),'Tasks')]"
    heading_task_page = "//h1[contains(text(),'Tasks')]"
    activity_filter = "//span[contains(text(),'All Activity Types')]"
    status_filter = "//span[contains(text(),'All Statuses')]"
    checkbox_schedule_call = "//span[contains(text(),'Scheduled Call')]"
    checkbox_meeting = "//span[contains(text(),'Meeting')]"
    checkbox_pending_status = "//span[contains(text(),'Pending')]"
    input_search = "//input[contains(@placeholder,'Search tasks...')]"
    btn_mark_complete = "//button[contains(text(),'Mark as Completed')]"
    textarea_notes = "//textarea[contains(@id,'task-completion-notes')]"
    btn_complete_task = "//button[contains(text(),'Complete Task')]"
    task_success_toast_message = "//div[contains(text(),'Success')]/following-sibling::div[contains(text(),'Task marked as completed successfully.')]"

    def redirect_to_tasks_tab(self):
        self.click(self.btn_tasks_tab)

    def complete_task(self,fetched_contact_name):
        # lead_page = LeadsPage(self.page)
        # contact_data = lead_page.add_lead_and_add_activities()
        # fetched_contact_name = contact_data["full_name"]

        self.redirect_to_tasks_tab()
        self.verify_visible(self.heading_task_page)
        self.click(self.activity_filter)
        self.click(self.checkbox_schedule_call)
        # self.page.pause()
        self.press_escape()
        self.click(self.status_filter)
        self.click(self.checkbox_pending_status)
        self.press_escape()
        self.fill(self.input_search, fetched_contact_name)
        self.click(f"//span[contains(text(),'{fetched_contact_name}')]")
        self.click(self.btn_mark_complete)
        self.fill(self.textarea_notes, RandomDataGenerator.random_comment())
        self.click(self.btn_complete_task)
        self.verify_visible(self.task_success_toast_message)
        self.click(self.checkbox_schedule_call)
        self.click(self.checkbox_meeting)
        self.press_escape()
        self.fill(self.input_search, fetched_contact_name)
        self.click(f"//span[contains(text(),'{fetched_contact_name}')]")
        self.click(self.btn_mark_complete)
        self.fill(self.textarea_notes, RandomDataGenerator.random_comment())
        self.click(self.btn_complete_task)
        self.verify_visible(self.task_success_toast_message)