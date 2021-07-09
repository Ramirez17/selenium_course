import time
from threading import Thread
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import unittest


class TestAbs(unittest.TestCase):
    # 1 тест
    def test_page1(self):
        hostname = "10.3.1.2"
        port = "8080"
        proxy_username = "ivaha_ay"
        proxy_password = "aJb6YkaD"

        chrome_options = Options()
        chrome_options.add_argument('--proxy-server={}'.format(hostname + ":" + port))
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1200, 1000)

        def enter_proxy_auth(proxy_username, proxy_password):
            time.sleep(1)
            pyautogui.typewrite(proxy_username)
            pyautogui.press('tab')
            pyautogui.typewrite(proxy_password)
            pyautogui.press('enter')

        def open_a_page(driver, url):
            driver.get(url)

        Thread(target=open_a_page, args=(driver, "https://demoqa.com/modal-dialogs")).start()
        Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

        try:
            driver.implicitly_wait(5)

            # кликаем на кнопку large modal
            driver.find_element_by_xpath("//button[@id='showLargeModal']").click()
            time.sleep(1)

            # проверяем, что в дереве есть элемент модального окна (заранее зная что его нет - тест упадет)
            big_modal = driver.find_element_by_xpath("//div[@class='modal-dialog modal-sm']")

            # проверяем наличие окна
            # try:
            #    big_modal = driver.find_element_by_xpath("//div[@class='modal-dialog modal-lg']")
            #    print("Yes big modal")
            # except NoSuchElementException:
            #    print("No big modal")


        finally:
            time.sleep(1)
            driver.quit()


if __name__ == "__main__":
    unittest.main()
