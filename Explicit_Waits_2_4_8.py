from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100')
    )
    button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='book']")))
    button.click()

    x_element = browser.find_element_by_xpath("//label//span[@id='input_value']")
    x = x_element.text

    def calt(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    result = calt(x)
    input_result = browser.find_element_by_xpath("//input[@class='form-control']")
    input_result.send_keys(str(result))

    button_finish = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='solve']")))
    button_finish.click()

finally:
    # time.sleep(4)
    # закрываем браузер после всех манипуляций
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()

