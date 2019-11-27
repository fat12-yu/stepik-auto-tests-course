#!/usr/bin/python

from selenium import webdriver
import time
import sys

try:
    browser = webdriver.Chrome()
    #browser = webdriver.Firefox()
    url = 'http://suninjuly.github.io/registration1.html'
    #url = 'http://suninjuly.github.io/registration2.html'
    browser.get(url)
    time.sleep(2) # Открываем урл и ждем 2 секунды
    inp = browser.find_element_by_css_selector('div.first_block input.form-control.first')
    inp.send_keys('Ivan')
    inp = browser.find_element_by_css_selector('div.first_block input.form-control.second')
    inp.send_keys('Petrov')
    inp = browser.find_element_by_css_selector('div.first_block input.form-control.third')
    inp.send_keys('ivan.petrov@gmail.com')
    time.sleep(4)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
except:
    print(sys.exc_info()) # если возникла ошибка, печатаем информацию об оной
else:
    print('All OK')
finally:
    time.sleep(2)
    browser.quit()
