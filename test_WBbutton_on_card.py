import time
from threading import Thread
import pyautogui
# import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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

        Thread(target=open_a_page, args=(driver, "https://www.wildberries.ru/")).start()
        Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

        try:
            # Ожидаем появления элементов
            driver.implicitly_wait(5)
            driver.find_element_by_xpath("//li[@class='simple-menu__item'][1]").click()
            driver.find_element_by_xpath("//div[@class='country__item']/label[2]/span[2]").click()
            driver.find_element_by_xpath("//input[@class='search-catalog__input j-search-input']").send_keys('стакан')
            time.sleep(2)
            driver.find_element_by_xpath(
                "//div[@class='autocomplete__content']/div[2]/div[@class='autocomplete__item j-suggestion']").click()

            # ищем кнопку "Быстрый просмотр"
            print('Наводимся')
            hover_block = driver.find_element_by_xpath("//div[@id='c15149740']")
            print('нашел карточку для наведения')
            hover = ActionChains(driver).move_to_element(hover_block)
            hover.perform()
            hide_button = driver.find_element_by_xpath(
                "//div[@id='catalog-content']//div[@id='c15149740'][1]//button[@class='quick-view j-open-product-popup'][1]")
            hide_button.click()

            # нажать "Добавить в корзину"
            driver.find_element_by_xpath("//div[@class='cart-btn-wrap']//button[@class='c-btn-main-lg-v1']").click()

            # нажать "Перейти в корзину"
            driver.find_element_by_xpath("//a[@class='c-btn-base-lg-v1 j-go-to-basket']").click()

        finally:
            time.sleep(1)
            driver.quit()


if __name__ == "__main__":
    unittest.main()

