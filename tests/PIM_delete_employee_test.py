from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_delete_employee(page):
    login = LoginPage(page)
    pim = PimPage(page)

    login.open()
    login.login("Admin", "admin123")

    page.wait_for_url("**dashboard**", timeout=15000)
    page.get_by_role("heading", name="Dashboard").wait_for(timeout=15000)

    pim.open_pim()
    pim.open_employee_list()
    pim.delete_employee()
    assert pim.is_delete_confirmation_displayed()
    pim.confirm_delete_employee()
    assert pim.is_success_delete_message_displayed()
    



    
    

    