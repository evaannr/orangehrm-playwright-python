from pages.login_page import LoginPage

def test_invalid_username(page):
    login = LoginPage(page)

    login.open()
    login.login("adminz", "admin123")

    assert login.is_invalid_credentials_displayed()