from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_add_employee(page):
    login = LoginPage(page)
    pim = PimPage(page)

    new_employee_first_name = "Aulia"
    new_employee_middle_name = "binti"
    new_employee_last_name = "Jackson"
    new_employee_id = "EMP333"
    new_employee_username = "amelia.jack"
    new_employee_password = "Password123" 
      

    login.open()
    login.login("Admin", "admin123")

    page.wait_for_url("**dashboard**", timeout=15000)
    page.get_by_role("heading", name="Dashboard").wait_for(timeout=15000)

    pim.open_pim()
    pim.open_add_employee()
    pim.fill_add_employee_form(new_employee_first_name, new_employee_middle_name, new_employee_last_name, new_employee_id, new_employee_username, new_employee_password)
    pim.save_add_employee_form()
    assert pim.is_success_add_message_displayed()

    pim.open_employee_list()
    pim.search_employee_by_name(new_employee_first_name)
    assert pim.is_employee_full_name_displayed(new_employee_first_name, new_employee_middle_name, new_employee_last_name)
