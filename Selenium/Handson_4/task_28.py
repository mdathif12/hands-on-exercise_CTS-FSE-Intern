from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

assert "simple-form-demo" in driver.current_url

print("URL Verification Passed")

driver.back()

print("Navigated Back Successfully")

driver.quit()