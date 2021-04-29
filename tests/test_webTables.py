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
        driver.set_window_size(1200, 1000)

        def enter_proxy_auth(proxy_username, proxy_password):
            time.sleep(1)
            pyautogui.typewrite(proxy_username)
            pyautogui.press('tab')
            pyautogui.typewrite(proxy_password)
            pyautogui.press('enter')

        def open_a_page(driver, url):
            driver.get(url)

        Thread(target=open_a_page, args=(driver, "https://demoqa.com/webtables")).start()
        Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

        try:
            # Задаем значения вводимых строк
            firstName = 'Andrew'
            lastName = 'Ivakha'
            userEmail = 'test@test.ru'
            age = '34'
            Salary = '10000000'
            department = 'US'

            # Ожидаем появления элементов
            driver.implicitly_wait(5)

            # Заполняем поля
            driver.find_element_by_xpath("//button[@id='addNewRecordButton']").click()
            driver.find_element_by_xpath("//input[@id='firstName']").send_keys("firstName")
            driver.find_element_by_xpath("//input[@id='lastName']").send_keys(lastName)
            driver.find_element_by_xpath("//input[@id='userEmail']").send_keys(userEmail)
            driver.find_element_by_xpath("//input[@id='age']").send_keys(age)
            driver.find_element_by_xpath("//input[@id='salary']").send_keys(Salary)
            driver.find_element_by_xpath("//input[@id='department']").send_keys(department)
            driver.find_element_by_xpath("//button[@id='submit']").click()
            time.sleep(1)

            # Находим ячейку с именем в добавленной нами строке
            firstName_print = driver.find_element_by_xpath(
                "//div[@class='rt-tbody']/div[@class='rt-tr-group'][4]//div[@class='rt-td'][1]").text

            # Проверяем, что строка присутствует
            assert firstName_print == firstName, "Отсутствует добавленная строка"
            if firstName_print == firstName:
                print("Строка добавлена")
        finally:
            time.sleep(1)
            driver.quit()


if __name__ == "__main__":
    unittest.main()
