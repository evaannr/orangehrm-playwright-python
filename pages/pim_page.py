import re
from playwright.sync_api import Page
from conftest import page


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
    
    def search_employee_by_job_title(self, employee_jobtitle):
        self.page.locator("div").filter(has_text=re.compile(r"^Job Title-- Select --$")).first.click()
        self.page.get_by_text(employee_jobtitle).click()
        self.page.get_by_role("button", name="Search").click()
    
    def is_employee_name_displayed(self, employee_name):
        locator = self.page.get_by_text(employee_name)
        locator.wait_for(timeout=10000)
        return locator.is_visible()

    def is_employee_id_displayed(self, employee_id):
        locator = self.page.get_by_text(employee_id)
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
    def is_employee_job_title_displayed(self, employee_jobtitle):
        locator = self.page.get_by_text(employee_jobtitle)
        locator.wait_for(timeout=10000)
        return locator.is_visible()

    def is_no_records_found_displayed(self):
        locator = self.page.locator("#oxd-toaster_1").get_by_text("No Records Found")
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
    def is_table_displayed(self):
        locator = self.page.get_by_role("row", name=" Id  First (& Middle) Name")
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
    def open_employee_details(self):
        self.page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
        
    
    def edit_employee_details(self, employee_first_name, employee_last_name, employee_id):
        self.page.get_by_role("textbox", name="First Name").click()
        self.page.get_by_role("textbox", name="First Name").fill(employee_first_name)
        self.page.get_by_role("textbox", name="Last Name").click()
        self.page.get_by_role("textbox", name="Last Name").fill(employee_last_name)
        self.page.get_by_role("textbox").nth(4).click()
        self.page.get_by_role("textbox").nth(4).fill(employee_id)
        
    
    def save_employee_details(self):
        self.page.locator("form").filter(has_text="Employee Full NameEmployee").get_by_role("button").click()
        
    
    def is_success_updated_message_displayed(self):
        locator = self.page.get_by_text("Successfully Updated")
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
    def is_employee_details_updated(self, employee_first_name, employee_last_name):
        row = self.page.get_by_role("row", name=re.compile(f".*{employee_first_name}.*{employee_last_name}.*"))
        row.wait_for(timeout=10000)
        return row.is_visible()
    
    def is_required_empty_message_displayed(self):
        locator = self.page.get_by_text("Required", exact=True)
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
    def is_not_excedeed_message_displayed(self):
        locator = self.page.get_by_text("Should not exceed 30")
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
    def delete_employee(self):
        self.page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()

    def is_delete_confirmation_displayed(self):
        locator = self.page.get_by_text("The selected record will be")
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
    def confirm_delete_employee(self):
        self.page.get_by_role("button", name=" Yes, Delete").click()

    def is_success_delete_message_displayed(self):
        locator = self.page.get_by_text("Successfully Deleted")
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
        

