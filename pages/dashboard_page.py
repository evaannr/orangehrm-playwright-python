from playwright.sync_api import Page

class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

    def logout(self):
        self.page.locator(".oxd-topbar-header-userarea li").click()

        self.page.get_by_role(
            "menuitem",
            name="Logout"
        ).click()