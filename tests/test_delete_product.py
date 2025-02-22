from page_objects.admin_page import AdminPage
from page_objects.login_admin_page import LoginAdminPage


def test_delete_product(driver, base_url):
    login_admin_page = LoginAdminPage(driver)

    login_admin_page.open(base_url, "/administration")
    login_admin_page.login_with_admin_creads(login="user", password="bitnami")

    admin_page = AdminPage(driver)
    product_nubmer_before_test = admin_page.number_of_product()

    admin_page.open_products_list()
    admin_page.select_product_in_list()
    admin_page.delete_product()
    driver.switch_to.alert.accept()
    product_nubmer_after_test = admin_page.number_of_product()

    assert product_nubmer_before_test - product_nubmer_after_test == 1
