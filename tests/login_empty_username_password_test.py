from pages.login_page import LoginPage

def test_empty_credentials(page):
    login = LoginPage(page)

    login.open()
    login.login("", "")

    assert login.are_both_required_messages_displayed()
    