from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep as time_sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

URL: str = "https://monkeytype.com/"
selector = """words"""

service = webdriver.ChromeService(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(URL)
time_sleep(10)

# find_elements(By.TAG_NAME, "letter")[0].text # out << m
element = driver.find_element(By.ID, selector).text.split()
