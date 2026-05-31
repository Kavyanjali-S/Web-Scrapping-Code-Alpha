from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Rajaraja_Cholan")

time.sleep(3)

quotes = driver.find_elements(By.CLASS_NAME, "quote")

for quote in quotes:

    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text

    print(text)
    print(author)
    print("----------------")

driver.quit()
