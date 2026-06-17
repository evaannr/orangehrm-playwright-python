from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)

    login.open()
    login.login("Admin", "admin123")

    assert "dashboard" in page.url.lower()

def is_required_message_displayed(self):
    locator = self.page.get_by_text("Required")
    locator.wait_for(timeout=10000)
    return locator.is_visible()