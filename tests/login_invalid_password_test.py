from pages.login_page import LoginPage

def test_invalid_password(page):
    login = LoginPage(page)

    login.open()
    login.login("Admin", "adminzzz")

    assert login.is_invalid_credentials_displayed()