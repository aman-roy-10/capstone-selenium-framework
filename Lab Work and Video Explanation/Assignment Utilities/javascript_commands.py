from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

# Create JavaScript executor
js = driver

# 1. Get page title using JavaScript
title = js.execute_script("return document.title;")
print("Page title:", title)

# 2. Scroll down using JavaScript
js.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Scrolled to bottom")

time.sleep(2)

# 3. Scroll back to top
js.execute_script("window.scrollTo(0, 0);")
print("Scrolled to top")

# 4. Highlight the Name input box
name_box = driver.find_element(By.ID, "name")

js.execute_script(
    "arguments[0].style.border='3px solid red';",
    name_box
)

print("Element highlighted")

time.sleep(2)

driver.quit()
