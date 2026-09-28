from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Open Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 2. Fill Input Boxes
driver.find_element(By.ID, "name").send_keys("John Doe")
driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
driver.find_element(By.ID, "phone").send_keys("9876543210")
driver.find_element(By.ID, "textarea").send_keys("123 Main Street")

# 3. Select Radio Button
driver.find_element(By.ID, "male").click()

# 4. Select Checkboxes
driver.find_element(By.ID, "sunday").click()
driver.find_element(By.ID, "monday").click()

# 5. Scroll down
driver.execute_script("window.scrollBy(0,500);")

# 6. Date Picker
date_input = driver.find_element(By.ID, "datepicker")
date_input.send_keys("08/31/2026")

# 7. Scroll to Submit button
submit_button = driver.find_element(
    By.XPATH, "//button[text()='Submit']"
)

driver.execute_script(
    "arguments[0].scrollIntoView(true);",
    submit_button
)

# 8. Click Submit
submit_button.click()

time.sleep(3)

# 9. Close browser
driver.quit()