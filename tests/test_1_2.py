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
            password = '222'  # заведомо неверный пароль
            expected_message = 'Неверный логин или пароль.'  # Ожидаемое сообщение об ошибке
            driver.implicitly_wait(5)
            driver.find_element_by_xpath("//*[@id='storage']").click()  # кликаем на dropdown для выбора хранилища
            driver.find_element_by_xpath("//*[@id='pr_id_2_list']/p-dropdownitem/li").click()  # кликаем на хранилище
            driver.find_element_by_xpath("//input[@id='user-name']").send_keys(login)  # вводим логин в поле
            driver.find_element_by_xpath("//*[@id='password']/div/input").send_keys(password)  # вводим пароль в поле
            driver.find_element_by_xpath("//button[@class='p-ripple p-element login-btn p-button p-component']").click()  # кликаем на кнопку Подключиться
            time.sleep(1)
            real_message = driver.find_element_by_xpath("//div[@class='message-panel']/p-toast/div/p-toastitem/div/div/div/div[2]").get_attribute("innerHTML")  # получаем текст всплывающего сообщения
            assert expected_message == real_message, 'Нет ожидаемого сообщения.'  # Проверяем соответствие ожидаемого сообщения полученному

        finally:
            driver.quit()


if __name__ == "__main__":
    unittest.main()
