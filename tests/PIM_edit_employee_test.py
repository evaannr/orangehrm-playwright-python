from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_edit_employee(page):
    login = LoginPage(page)
    pim = PimPage(page)

    update_employee_first_name = "editt22"
    update_employee_last_name = "testedd222"
    update_employee_id = "0889"

    login.open()
    login.login("Admin", "admin123")

    page.wait_for_url("**dashboard**", timeout=15000)
    page.get_by_role("heading", name="Dashboard").wait_for(timeout=15000)

    pim.open_pim()
    pim.open_employee_list()
    pim.open_employee_details()
    pim.edit_employee_details(update_employee_first_name, update_employee_last_name, update_employee_id)
    pim.save_employee_details()
    assert pim.is_success_updated_message_displayed()
    pim.open_employee_list()
    pim.search_employee_by_name(update_employee_first_name)
    assert pim.is_employee_details_updated(update_employee_first_name, update_employee_last_name)





    
    

    