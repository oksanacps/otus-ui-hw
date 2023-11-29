import random

from page_objects.admin_page import AdminPage
from page_objects.login_admin_page import LoginAdminPage
from page_objects.admin_home_page import AdminHomePage


def test_add_product(driver, base_url):
    login_admin_page = LoginAdminPage(driver)

    login_admin_page.open(base_url, '/admin')
    login_admin_page.login_with_admin_creads(login='user', password='bitnami')

    admin_page = AdminPage(driver)
    product_nubmer_before_test = admin_page.number_of_product()
    product_name, meta_tag, model = 'product_name' + str(random.randint(1, 100)), \
        'meta_tag' + str(random.randint(1, 100)), 'model' + str(random.randint(1, 100))

    admin_page.open_products_list()
    admin_page.open_add_product_form()
    admin_page.fill_required_fields_for_new_product()
    admin_page.click_save_button()
    product_nubmer_after_test = admin_page.number_of_product()
    product_name_result, model_result = admin_page.get_attributes_new_product()

    assert product_nubmer_after_test - product_nubmer_before_test == 1
    assert product_name == product_name_result
    assert model == model_result



