from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.lambdatest.com/selenium-playground/")

current_size = driver.get_window_size()

print("Current Window Size:")
print(current_size)

driver.set_window_size(1280, 800)

new_size = driver.get_window_size()

print("Updated Window Size:")
print(new_size)

driver.quit()