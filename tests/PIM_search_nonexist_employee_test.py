from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_search_nonexistent_employee(page):
    login = LoginPage(page)
    pim = PimPage(page)

    search_employee_name = "Bandot"

    login.open()
    login.login("Admin", "admin123")

    page.wait_for_url("**dashboard**", timeout=15000)
    page.get_by_role("heading", name="Dashboard").wait_for(timeout=15000)

    pim.open_pim()
    pim.open_employee_list()
    pim.search_employee_by_name(search_employee_name)
    assert pim.is_no_records_found_displayed()



    
    

    