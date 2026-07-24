from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# By.ID
element_id = driver.find_element(By.ID, "user-message")
print("ID Locator Works")

# By.NAME
element_name = driver.find_element(By.NAME, "user-message")
print("NAME Locator Works")

# By.CLASS_NAME
element_class = driver.find_element(By.CLASS_NAME, "form-control")
print("CLASS_NAME Locator Works")

# By.TAG_NAME
element_tag = driver.find_element(By.TAG_NAME, "input")
print("TAG_NAME Locator Works")

# By.XPATH Absolute
try:
    element_abs = driver.find_element(
        By.XPATH,
        "/html/body/div/div/section[1]/div/div/div[1]/div/input"
    )
    print("ABSOLUTE XPATH Works")
except:
    print("Absolute XPath may vary depending on page updates")

# By.XPATH Relative
element_rel = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)
print("RELATIVE XPATH Works")

driver.quit()