import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Test Data ~ put your user credentials here to run test 
username = "YourEmail"
password = "YourPassword"

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
  
# Go to profile page
driver.find_element(By.CSS_SELECTOR, ".hui-globaluseritem__display-name").click()
driver.find_element(By.CSS_SELECTOR, ".hui-globalusermenu__personal-items span").click()
time.sleep(5)

# Check that we are on the acutal profile page URL
URL = driver.current_url
assert 'https://www.hudl.com/profile/' == URL,"Not on profile page"
driver.quit()

# Comment out the above assertion and run with the below to check if test is working
#URL = driver.current_url
#assert 'https://www.google.com' == URL,"Test is working!"
#driver.quit()