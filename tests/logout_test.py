# tests/logout_test.py

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_logout(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open()
    login.login("Admin", "admin123")

    dashboard.logout()

    page.wait_for_url("**/auth/login", timeout=15000)

    assert "login" in page.url.lower()