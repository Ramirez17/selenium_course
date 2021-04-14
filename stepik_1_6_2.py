import time
from threading import Thread
import pyautogui
import math
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

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

Thread(target=open_a_page, args=(driver, "http://suninjuly.github.io/find_xpath_form")).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

# Метод get сообщает браузеру, что нужнivaha_ay aJb6YkaD
# о открыть сайт по указанной ссылке
#driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(3)


try:
    #from selenium.webdriver.common.by import By


    input1 = driver.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")

    button = driver.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()


# После выполнения всех действий мы не должны забыть закрыть окно браузера
finally:
    time.sleep(15)
    driver.quit()
