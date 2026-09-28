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

# Search for a specific product
search_product = "Laptop"

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    if cells:
        product_name = cells[1].text

        if product_name == search_product:
            print("Product found:", product_name)
            print("Product ID:", cells[0].text)
            print("Product Price:", cells[2].text)
            break

driver.quit()