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

Thread(target=open_a_page, args=(driver, "http://suninjuly.github.io/registration1.html")).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

#Таймаут для загрузки страницы после авторизации на прокси
time.sleep(3)

try:
    input1 = driver.find_element_by_xpath("//div[@class='first_block']/div/input[@class='form-control first']")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_xpath("//div[@class='first_block']/div/input[@class='form-control second']")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input[@class='form-control third']")
    input3.send_keys("example@email.com")
    time.sleep(1)
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    driver.quit()
