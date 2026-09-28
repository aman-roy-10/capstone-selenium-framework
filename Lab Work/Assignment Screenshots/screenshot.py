from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")

# Take screenshot of the complete webpage
driver.save_screenshot("homepage.png")

print("Screenshot saved successfully")

driver.quit()