#!/usr/bin/python

from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    browser = webdriver.Chrome()

    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    el = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'),'100')
    )
    button = browser.find_element_by_id("book")
    button.click()

    el = browser.find_element_by_id('input_value')
    x = el.text
    x = str(math.log(abs(12*math.sin(int(x)))))
    el = browser.find_element_by_id('answer')
    el.send_keys(x)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'solve'))
            )
    button.click()

finally:
    time.sleep(15)
    browser.quit()
