from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()

driver.find_element(
    By.CSS_SELECTOR,
    "button[onclick='jsPrompt()']"
).click()

time.sleep(2)

alert_window = driver.switch_to.alert

print(alert_window.text)

alert_window.send_keys("Aman")

alert_window.accept()

time.sleep(2)

driver.quit()