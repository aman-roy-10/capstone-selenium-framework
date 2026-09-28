from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.example.com")
print("Selenium test executed successfully!")
driver.quit()
