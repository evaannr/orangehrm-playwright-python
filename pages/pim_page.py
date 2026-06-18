from playwright.sync_api import Page

class PimPage:

    def __init__(self, page: Page):
        self.page = page

    def open_pim(self):
        self.page.get_by_role("link", name="PIM").click()
    

    def open_employee_list(self):
        self.page.get_by_role("link", name="Employee List").click()

    def search_employee_by_name(self, employee_name):
        self.page.get_by_role("textbox", name="Type for hints...").first.fill(employee_name)
        self.page.get_by_role("button", name="Search").click()

    def search_employee_by_id(self, employee_id):
        self.page.get_by_role("textbox").nth(2).fill(employee_id)
        self.page.get_by_role("button", name="Search").click()
    
    def is_employee_name_displayed(self, employee_name):
        locator = self.page.get_by_text(employee_name)
        locator.wait_for(timeout=10000)
        return locator.is_visible()

    def is_employee_id_displayed(self, employee_id):
        locator = self.page.get_by_text(employee_id)
        locator.wait_for(timeout=10000)
        return locator.is_visible()