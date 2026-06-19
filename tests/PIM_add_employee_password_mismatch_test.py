from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_add_employee_password_mismatch(page):
    login = LoginPage(page)
    pim = PimPage(page)

    new_employee_first_name = "Jaka"
    new_employee_middle_name = "binti"
    new_employee_last_name = "Smith"
    new_employee_id = "EMP0000"
    new_employee_username = "jackbintismith"
    new_employee_password = "Password123"
    new_employee_confirm_password = "Password1234"

    login.open()
    login.login("Admin", "admin123")

    page.wait_for_url("**dashboard**", timeout=15000)
    page.get_by_role("heading", name="Dashboard").wait_for(timeout=15000)

    pim.open_pim()
    pim.open_add_employee()
    pim.fill_add_employee_basic_info_form(new_employee_first_name, new_employee_middle_name, new_employee_last_name, new_employee_id)
    pim.enabled_create_login_details()
    pim.fill_add_employee_login_details_form(new_employee_username, new_employee_password, new_employee_confirm_password)
    pim.save_add_employee_form()
    assert pim.is_password_mismatch_message_displayed()