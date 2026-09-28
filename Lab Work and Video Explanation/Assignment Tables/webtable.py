from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Open practice website
driver.get("https://testautomationpractice.blogspot.com/")

# Find the table
table = driver.find_element(By.ID, "productTable")

# Get all rows
rows = table.find_elements(By.TAG_NAME, "tr")

print("Number of rows:", len(rows))

# Print every row
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    if cells:
        row_data = [cell.text for cell in cells]
        print(row_data)

driver.quit()