from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class TestButtonAddItem:
    def test_item_page_has_add_button(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        try:
            add_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        except NoSuchElementException:
            add_button = []
        # sleep(10)
        assert add_button, f"Add button is not found"
