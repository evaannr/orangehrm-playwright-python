from pages.login_page import LoginPage

def test_empty_username(page):
    login = LoginPage(page)

    login.open()
    login.login("", "admin123")

    assert login.is_required_message_displayed()