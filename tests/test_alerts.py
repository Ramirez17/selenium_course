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

        Thread(target=open_a_page, args=(driver, "https://demoqa.com/alerts")).start()
        Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

        try:
            driver.implicitly_wait(5)

            # Button1
            driver.find_element_by_xpath("//button[@id='alertButton']").click()
            alert1 = driver.switch_to.alert
            text1 = alert1.text
            print(text1)
            alert1.accept()

            # Button2
            driver.find_element_by_xpath("//button[@id='timerAlertButton']").click()
            wait = WebDriverWait(driver, 10)
            wait.until(EC.alert_is_present())
            alert2 = driver.switch_to.alert
            time.sleep(3)
            alert2.accept()

        finally:
            time.sleep(4)
            driver.quit()


if __name__ == "__main__":
    unittest.main()
