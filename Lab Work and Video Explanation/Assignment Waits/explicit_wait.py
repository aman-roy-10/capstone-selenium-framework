from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# Create explicit wait
wait = WebDriverWait(driver, 10)

# Click Enable
enable_button = driver.find_element(
    By.XPATH,
    "//button[text()='Enable']"
)

enable_button.click()

# Wait until the input becomes enabled/clickable
input_box = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#input-example input")
    )
)

print("Input enabled:", input_box.is_enabled())

# Enter text
input_box.send_keys("Selenium")

print("Text entered successfully")

driver.quit()