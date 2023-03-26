import time, math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.mark.parametrize('test_links', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_find_correct_number(browser):
    browser.implicitly_wait(5)
    link = f"https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys("silenoksergey34@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("19971222")
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
    answer = math.log(int(time.time()))
    # text_area = WebDriverWait(browser, 5).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea"))
    # )
    # text_area.send_keys(answer)
    browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(answer)
    WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        ).click()

    # browser.find_element(By.CLASS_NAME, "submit-submission").click()

    quest_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert quest_text == 'Correct!', 'Stepic не принял значение'



