from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open the practice website
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default")

driver.maximize_window()

time.sleep(2)

# Switch to the iframe
iframe = driver.find_element(By.ID, "iframeResult")
driver.switch_to.frame(iframe)

# Find the heading inside the iframe
heading = driver.find_element(By.TAG_NAME, "h1")

print("Text inside iframe:", heading.text)

time.sleep(3)

# Switch back to the main page
driver.switch_to.default_content()

print("Switched back to main page")

time.sleep(2)

driver.quit()