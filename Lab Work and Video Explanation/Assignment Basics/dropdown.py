from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

dropdown = Select(
    driver.find_element(By.ID, "dropdown-class-example")
)

dropdown.select_by_visible_text("Option1")

time.sleep(2)