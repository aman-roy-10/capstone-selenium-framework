from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://text-compare.com/")

# Task 1
input1 = driver.find_element(By.XPATH, "//*[@id='inputText1']")
input1.send_keys("Welcome to Selenium.")
time.sleep(2)

input2 = driver.find_element(By.XPATH, "//*[@id='inputText2']")

# Task 2 - Copy whatever is there on the left panel to the right
act = ActionChains(driver)

act.click(input1).key_down("CTRL").send_keys("a").key_up("CTRL")

act.key_down("CTRL").send_keys("c").key_up("CTRL")

act.click(input2)

act.key_down("CTRL").send_keys("v").key_up("CTRL")

act.perform()

time.sleep(3)