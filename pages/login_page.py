from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            timeout=120000
            
        )


    def login(self, username, password):
        self.page.get_by_role(
            "textbox",
            name="Username"
        ).wait_for(timeout=10000)

        self.page.get_by_role(
            "textbox",
            name="Username"
        ).fill(username)

        self.page.get_by_role(
            "textbox",
            name="Password"
        ).fill(password)

        self.page.get_by_role(
            "button",
            name="Login"
        ).click()

    def is_invalid_credentials_displayed(self):
        locator = self.page.get_by_text("Invalid credentials")
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
    def is_required_message_displayed(self):
        locator = self.page.get_by_text("Required")
        locator.wait_for(timeout=10000)
        return locator.is_visible()
    
    def are_both_required_messages_displayed(self):
        locator1 = self.page.get_by_text("Required").first
        locator2 = self.page.get_by_text("Required").nth(1)
        locator1.wait_for(timeout=10000)
        locator2.wait_for(timeout=10000)
        return locator1.is_visible() and locator2.is_visible()