from playwright.sync_api import Page

class DashboardPage:

    def __init__(self, page):
        self.page = page

    def logout(self):
        self.page.locator("span").filter(
            has_text="manda user"
        ).click()

        self.page.get_by_role(
            "menuitem",
            name="Logout"
        ).click()