from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")

time.sleep(3)

# Find source and target elements
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

# Create ActionChains object
actions = ActionChains(driver)

# Drag source and drop it on target
actions.drag_and_drop(source, target)

# Perform the action
actions.perform()

time.sleep(3)