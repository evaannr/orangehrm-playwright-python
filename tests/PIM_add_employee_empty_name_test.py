from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_add_employee_with_empty_names(page):
    login = LoginPage(page)
    pim = PimPage(page)

    new_employee_first_name = ""
    new_employee_middle_name = "binti"
    new_employee_last_name = "" 
    new_employee_id = "EMP222"

    login.open()
    login.login("Admin", "admin123")

    page.wait_for_url("**dashboard**", timeout=15000)
    page.get_by_role("heading", name="Dashboard").wait_for(timeout=15000)

    pim.open_pim()
    pim.open_add_employee()
    pim.fill_add_employee_basic_info_form(new_employee_first_name, new_employee_middle_name, new_employee_last_name, new_employee_id)

    pim.save_add_employee_form()
    assert pim.is_first_required_message_displayed()
