from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(
    "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo"
)

driver.find_element(
    By.ID,
    "autoclosable-btn-success"
).click()

alert = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

print("Alert Text:")
print(alert.text)

assert "successfully" in alert.text.lower()

print("Explicit Wait Successful")

driver.quit()