from pages.login_page import LoginPage

def test_empty_password(page):
    login = LoginPage(page)

    login.open()
    login.login("Admin", "")

    assert login.is_required_message_displayed()