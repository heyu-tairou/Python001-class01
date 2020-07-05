from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im')
    time.sleep(1)
    
    btm1 = browser.find_element_by_xpath('//button[@class="login-button btn_hover_style_8"]')
    btm1.click()

    time.sleep(1)
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('13430232499')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('3379227z')
    time.sleep(1)
    browser.find_element_by_xpath('//button[text()="立即登录"]').click()
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()
    