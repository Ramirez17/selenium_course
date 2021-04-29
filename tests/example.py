import time
from threading import Thread
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

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
    #Задаем значения вводимых строк
    #Name = 'Andrew'

    #Ожидаем появления элементов
    driver.implicitly_wait(5)

    #Заполняем поля
    driver.find_element_by_xpath("//button[@id='submit']").click()
    element = driver.find_element_by_xpath("//input[@id='firstName']").value_of_css_property('border-corol')
    print(element)
finally:
    time.sleep(1)
    driver.quit()
