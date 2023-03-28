import time, math, pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('test_links', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_find_correct_number(browser, test_links):
    browser.implicitly_wait(50)
    link = f"https://stepik.org/lesson/{test_links}/step/1"
    browser.get(link)
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys("silenoksergey34@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("19971222")
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
    time.sleep(5)
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea"))).send_keys(math.log(int(time.time())))
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
    finnaly_text = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "again-btn.white"))).click()
    assert finnaly_text == 'Correct!', f"Финальный текст : {finnaly_text}"
