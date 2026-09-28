from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

else:
    raise Exception("Invalid browser name. Please choose 'chrome'")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value='radio2']").click()

time.sleep(2)