from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)

    login.open()
    login.login("Admin", "admin123")

    assert "dashboard" in page.url.lower()