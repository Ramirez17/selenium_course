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
Thread(target=open_a_page, args=(driver, "http://suninjuly.github.io/alert_accept.html")).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

time.sleep(3)
try:
    driver.find_element_by_xpath("//div[@class='container']/button[@class='btn btn-primary']").click()
    confirm = driver.switch_to.alert
    confirm.accept()
    num = driver.find_element_by_xpath("//label/span[@id='input_value']")
    x = num.text
    time.sleep(1)
    y = calc(x)
    input1 = driver.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)
    driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    print(driver.switch_to.alert.text)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    driver.quit()
# не забываем оставить пустую строку в конце файла
