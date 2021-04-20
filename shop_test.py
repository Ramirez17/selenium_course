import time
from threading import Thread
import pyautogui
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
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

        def enter_proxy_auth(proxy_username, proxy_password):
            time.sleep(1)
            pyautogui.typewrite(proxy_username)
            pyautogui.press('tab')
            pyautogui.typewrite(proxy_password)
            pyautogui.press('enter')

        def open_a_page(driver, url):
            driver.get(url)

        Thread(target=open_a_page, args=(driver, "https://demoqa.com/text-box")).start()
        Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

        driver.implicitly_wait(5)
        fullNameValue = "Andrew"
        fullNameValue1 = "Andrew1"
        fullName = driver.find_element_by_xpath("//input[@id='userName']")
        fullName.send_keys(fullNameValue)

        driver.find_element_by_xpath("//button[@id='submit']").click()

        nameResult = driver.find_element_by_xpath("//p[@id='name']").text
        assert fullNameValue1 == nameResult, "Имя введено некорректно"

        time.sleep(1)
        # закрываем браузер после всех манипуляций
        driver.quit()

if __name__ == "__main__":
    unittest.main()

