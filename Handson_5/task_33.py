from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# CSS Selector using ID
css1 = driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)
print("CSS by ID Works")

# CSS Selector using Attribute
css2 = driver.find_element(
    By.CSS_SELECTOR,
    "input[name='user-message']"
)
print("CSS by Attribute Works")

# CSS Selector using Parent > Child
css3 = driver.find_element(
    By.CSS_SELECTOR,
    "div > input"
)
print("CSS Parent > Child Works")

driver.quit()