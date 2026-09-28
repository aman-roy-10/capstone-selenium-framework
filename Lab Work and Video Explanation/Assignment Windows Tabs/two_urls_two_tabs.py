from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open first URL
driver.get("https://www.google.com")

# Open a new tab
driver.switch_to.new_window("tab")

# Open second URL
driver.get("https://www.youtube.com")

# Keep browser open
input("Press Enter to close the browser...")

driver.quit()