from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_search_valid_employee_name(page):
    login = LoginPage(page)
    pim = PimPage(page)

    employee_name = "Amelia"

    login.open()
    login.login("Admin", "admin123")

    page.wait_for_url("**dashboard**", timeout=15000)
    page.get_by_role("heading", name="Dashboard").wait_for(timeout=15000)

    pim.open_pim()
    pim.open_employee_list()
    pim.search_employee_by_name(employee_name)
    assert pim.is_employee_name_displayed(employee_name)



    
    

    