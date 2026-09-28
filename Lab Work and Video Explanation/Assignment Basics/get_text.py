from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Open practice website
driver.get("https://testautomationpractice.blogspot.com/")

# Find the heading
heading = driver.find_element(By.TAG_NAME, "h1")

# Get the text
text = heading.text

print("Text of the element:", text)

driver.quit()