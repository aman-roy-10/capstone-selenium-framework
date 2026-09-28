from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 1. Open the first URL
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 2. Store the first tab's window handle
parent_window = driver.current_window_handle
print("Parent window:", parent_window)

# 3. Click "New Tab"
new_tab = driver.find_element(
    By.XPATH,
    "//button[text()='New Tab']"
)
new_tab.click()

# 4. Get all open window/tab handles
windows = driver.window_handles
print("All windows:", windows)

# 5. Switch to the new tab
for window in windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break

print("Switched to new tab")

# 6. Perform a task on the new tab
# The new tab contains a text box.
driver.find_element(By.ID, "input1").send_keys("Hello Selenium")

print("Task completed on new tab")

time.sleep(2)

# 7. Close the new tab
driver.close()

# 8. Switch back to the first tab
driver.switch_to.window(parent_window)

print("Back to first tab")

# 9. Write your name in the first tab
driver.find_element(By.ID, "name").send_keys("Aman")

print("Name entered successfully")

time.sleep(3)

# 10. Close browser
driver.quit()