import time
from threading import Thread
import pyautogui
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
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

Thread(target=open_a_page, args=(driver, "http://suninjuly.github.io/math.html")).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

#Таймаут для загрузки страницы после авторизации на прокси
time.sleep(2)

try:
    x_element = driver.find_element_by_xpath("//label/span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input_answer = driver.find_element_by_xpath("//input[@id='answer']")
    input_answer.send_keys(y)

    option1 = driver.find_element_by_xpath("//input[@id='robotCheckbox']")
    option1.click()

    option2 = driver.find_element_by_xpath("//input[@id='robotsRule']")
    option2.click()

    button = driver.find_element_by_xpath("//button[@class='btn btn-default']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    driver.quit()

