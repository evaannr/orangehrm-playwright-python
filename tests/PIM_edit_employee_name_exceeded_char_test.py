from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_edit_name_exceeded_employee(page):
    login = LoginPage(page)
    pim = PimPage(page)

    update_employee_first_name = "asbdndjkasdoandn300000nksdnsndnfijhewuhfjnjnjaw"
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
    assert pim.is_exceeded_30_char_message_displayed()
    





    
    

    