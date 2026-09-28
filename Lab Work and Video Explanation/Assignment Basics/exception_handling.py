from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

try:
    print("Searching for element...")

    # This ID intentionally does not exist
    element = driver.find_element(By.ID, "wrong_element_id")

    element.click()

except NoSuchElementException:
    print("NoSuchElementException handled successfully")

finally:
    print("Closing browser")
    driver.quit()