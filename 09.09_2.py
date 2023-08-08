import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://strizhechenko.github.io/resume.html" # (меняем название сайта(в поисковой строке)
browser = webdriver.Chrome()
browser.get(link)


button = browser.find_element(By.XPATH, '/html/body/header/div/nav/div/a')
button.click() # Нажать на кнопку

div1 = browser.find_element(By.XPATH, '//*[@id="опыт-работы"]')
div1 = div1.text

assert 'Опыт работы' == div1
# закрываем браузер после всех манипуляций
time.sleep(20)
browser.quit()