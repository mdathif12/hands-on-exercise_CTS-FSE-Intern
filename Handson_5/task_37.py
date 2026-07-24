from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo"

# ------------------------
# Explicit Wait
# ------------------------

driver.get(url)

start = time.time()

driver.find_element(
    By.ID,
    "autoclosable-btn-success"
).click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

end = time.time()

print("Explicit Wait Time:", round(end - start, 2), "seconds")

# ------------------------
# Sleep
# ------------------------

driver.get(url)

start = time.time()

driver.find_element(
    By.ID,
    "autoclosable-btn-success"
).click()

time.sleep(3)

driver.find_element(
    By.CSS_SELECTOR,
    ".alert-success"
)

end = time.time()

print("Sleep Time:", round(end - start, 2), "seconds")

driver.quit()