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

        Thread(target=open_a_page, args=(driver, "https://demoqa.com/automation-practice-form")).start()
        Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

        try:
            # Задаем значения вводимых строк
            succes_border = 'rgb(40, 167, 69)'
            firstName = 'Andrew'
            lastName = 'Ivakha'
            mobileNumber = '9150944414'

            # Ожидаем появления элементов
            driver.implicitly_wait(5)

            # Заполняем inputы
            driver.find_element_by_xpath("//input[@id='firstName']").send_keys(firstName)
            driver.find_element_by_xpath("//input[@id='lastName']").send_keys(lastName)
            driver.find_element_by_xpath(
                "//input[@id='gender-radio-1']/following::label[@class='custom-control-label'][1]").click()
            driver.find_element_by_xpath("//input[@id='userNumber']").send_keys(mobileNumber)

            # Скроллим до кнопки
            driver.execute_script("window.scrollBy(0, 90);")

            # Ищем Submit и нажимаем
            submit = driver.find_element_by_xpath("//button[@id='submit']")
            submit.click()
            time.sleep(2)

            # Ищем значения bordеr-color у полей First Name, Last Name и Mobile Number
            firstName_border = driver.find_element_by_xpath(
                "//input[@id='firstName' and @class=' mr-sm-2 form-control']").value_of_css_property('border-color')
            # Сравниваем с эталонным значением - с зеленым (переменная succes_border)
            if firstName_border != succes_border:
                print("Не заполнены обязательные поля")

            driver.find_element_by_xpath("//button[@id='closeLargeModal']").click()
            print("Все обязательные поля заполнены. Цвет - ", firstName_border)
        finally:
            time.sleep(1)
            driver.quit()


if __name__ == "__main__":
    unittest.main()
