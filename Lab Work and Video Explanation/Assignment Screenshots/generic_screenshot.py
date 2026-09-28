from selenium import webdriver
from datetime import datetime


def take_screenshot(driver, name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"

    driver.save_screenshot(filename)

    print("Screenshot saved:", filename)


driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")

# Call reusable screenshot function
take_screenshot(driver, "homepage")

driver.quit()