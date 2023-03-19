import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'lesson2.2_7.txt')

try:
    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    first_name.send_keys("Sergey")
    last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    last_name.send_keys("Silenok")
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    email.send_keys("mail")

    file_button = browser.find_element(By.ID, "file")
    file_button.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit_button.click()


finally:
    time.sleep(5)
    browser.quit()
