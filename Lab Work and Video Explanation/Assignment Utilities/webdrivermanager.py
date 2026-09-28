from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    driver.get("https://testautomationpractice.blogspot.com")

    driver.maximize_window()

    driver.find_element(
        By.XPATH, "//input[@id='email']"
    ).send_keys("test@example.com")

    time.sleep(2)