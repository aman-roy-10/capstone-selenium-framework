from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Set implicit wait
driver.implicitly_wait(10)

# Open page
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# Click Enable
driver.find_element(
    By.XPATH,
    "//button[text()='Enable']"
).click()

# Find the input element
input_box = driver.find_element(
    By.CSS_SELECTOR,
    "#input-example input"
)

print("Input found successfully")
print("Input enabled:", input_box.is_enabled())

driver.quit()