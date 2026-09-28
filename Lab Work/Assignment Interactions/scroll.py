from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://text-compare.com")

time.sleep(5)

print("Windows:", driver.window_handles)
print("URL:", driver.current_url)

# Scroll to bottom
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)

print("Scroll completed")

time.sleep(5)