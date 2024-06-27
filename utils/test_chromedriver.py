from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
options = webdriver.ChromeOptions()

# Create an instance of Chrome WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open Google and print the title
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
