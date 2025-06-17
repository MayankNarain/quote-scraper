from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com")

wait = WebDriverWait(driver, 10)

quotes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

print("Quotes:\n")

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    print(f"{text} — {author}")

driver.quit()
