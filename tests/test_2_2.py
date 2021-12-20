import time
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import unittest


class TestAbs(unittest.TestCase):
    def test_1_1(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1200, 1000)
        driver.get("http://polynom-web.klmn.ascon.local")

        try:
            login = 'admin'  # логин
            password = '111'  # пароль
            search_query = 'болт' # поисковый запрос
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//*[@id='storage']").click()  # кликаем на dropdown для выбора хранилища
            driver.find_element_by_xpath("//*[@id='pr_id_2_list']/p-dropdownitem/li").click()  # кликаем на хранилище
            driver.find_element_by_xpath("//input[@id='user-name']").send_keys(login)  # вводим логин
            driver.find_element_by_xpath("//*[@id='password']/div/input").send_keys(password)  # вводим пароль
            driver.find_element_by_xpath(
                "//button[@class='p-ripple p-element login-btn p-button p-component']").click()  # кликаем Подключиться
            driver.find_element_by_xpath(
                "//div[@class='navbar-center-content']//input").send_keys(search_query)  # вводим поисковый запрос
            driver.find_element_by_xpath("//ul[@role='listbox']/li[1]").click()
            time.sleep(3)

        finally:
            driver.quit()


if __name__ == "__main__":
    unittest.main()
