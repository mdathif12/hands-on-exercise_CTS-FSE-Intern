from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

# XPath text()
label = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print("Label Found:")
print(label.text)

# XPath contains()
labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("\nAll Option Labels")

for item in labels:
    print(item.text)

driver.quit()