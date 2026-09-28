from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# 1. Select Radio Button (First Choice: Radio1)
driver.find_element(By.XPATH, "//input[@value='radio1']").click()

# 2. Select Country (Germany without typing)
autocomplete_input = driver.find_element(By.ID, "autocomplete")
driver.execute_script("arguments[0].value = 'Germany';", autocomplete_input)

# 3. Dropdown (First Choice: Option1)
dropdown = driver.find_element(By.ID, "dropdown-class-example")
dropdown.find_element(By.XPATH, ".//option[@value='option1']").click()

# 4. Checkbox (First Choice: Option1)
driver.find_element(By.ID, "checkBoxOption1").click()

time.sleep(2)
driver.quit()