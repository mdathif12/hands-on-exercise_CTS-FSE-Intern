from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(
    "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo"
)

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "autoclosable-btn-success")
    )
)

button.click()

print("Button Clicked Successfully")

driver.quit()