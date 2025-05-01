import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Test Data ~ non working login
username = "notarealemail@hudl.com"
password = "not a realpassword"

# Load page
driver = webdriver.Chrome()
driver.get('https://www.hudl.com/')
time.sleep(5) 

# Login
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.CSS_SELECTOR, ".subnav__item:nth-child(1) > .subnavitem__label").click()
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.NAME, "action").click()
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.NAME, "action").click()

# Sit around a bit
time.sleep(5)
  
# Assert error is present to user
elements = driver.find_elements(By.ID, "error-element-password")
assert len(elements) > 0
driver.quit()




