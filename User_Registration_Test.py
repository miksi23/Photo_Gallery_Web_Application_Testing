
import time

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://demo.baasic.com/angular/starterkit-photo-gallery/main')
mouse_hovering = ActionChains(browser)
#menu link from home page
logo_button=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
mouse_hovering.move_to_element(logo_button).click().perform()
time.sleep(3)
#registration
register_option=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[3]/span")
mouse_hovering.move_to_element(register_option).click().perform()
time.sleep(3)
email_field=browser.find_element(By.ID, "email")
email_field.send_keys("mirjanavelagic@gmail.com")
time.sleep(1)
username_register_field=browser.find_element(By.ID, "userName")
username_register_field.send_keys("kolacic2")
time.sleep(1)
password_register_field=browser.find_element(By.ID, "password")
password_register_field.send_keys("Zeljana13507")
time.sleep(1)
confirm_password_field=browser.find_element(By.ID, "confirmPassword")
confirm_password_field.send_keys("Zeljana13507")
time.sleep(1)
register_button=browser.find_elements(By.TAG_NAME, "button")[0]
register_button.click()
time.sleep(5)
browser.save_screenshot("user_registration.png")