import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
user_name = driver.find_element(By.ID, "user-name")
user_name = driver.find_element(By.NAME, "user-name")
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name = driver.find_element(By.CSS_SELECTOR, "//input[@id='user-name']"
user_name.send_keys('standard_user')
    //input[@value='Login']
time.sleep(10)
driver.quit()