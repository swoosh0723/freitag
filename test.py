from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')
url = 'https://google.com'
driver.get(url)

driver.find_element(By.CSS_SELECTOR, '.gLFyf.gsfi').send_keys(
    "되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라되어라")

# msg = 'hello world'
# print(msg)
