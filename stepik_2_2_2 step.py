import time
from threading import Thread
import pyautogui

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
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

Thread(target=open_a_page, args=(driver, "http://suninjuly.github.io/selects1.html")).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

time.sleep(3)
try:
    select1 = driver.find_element_by_xpath("//h2/span[@id='num1']")
    x1 = select1.text

    x2 = str(x1)

    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_value(x2)  # ищем элемент с текстом "Python"

    #driver.find_element_by_xpath("//button[@class='btn btn-default']").click()




finally:
# успеваем скопировать код за 30 секунд
    time.sleep(1)
# закрываем браузер после всех манипуляций
    driver.quit()