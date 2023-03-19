from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "http://suninjuly.github.io/find_link_text"

next_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_link = browser.find_element(By.PARTIAL_LINK_TEXT, next_link)
    find_link.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Sergey")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Silenok")

    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Magnitogorsk")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла