from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Open practice website
driver.get("https://testautomationpractice.blogspot.com/")

# Find the name input box
name_box = driver.find_element(By.ID, "name")

# Get the value of the "placeholder" attribute
placeholder_value = name_box.get_attribute("placeholder")

print("Placeholder value:", placeholder_value)

# Get the value of the "type" attribute
type_value = name_box.get_attribute("type")

print("Type attribute:", type_value)

driver.quit()