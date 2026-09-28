from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    time.sleep(2)

    print("Page title:", driver.title)

finally:
    driver.quit()