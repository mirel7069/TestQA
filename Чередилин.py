import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://yohoho.cc/" # (меняем название сайта(в поисковой строке)
browser = webdriver.Chrome()
browser.get(link)

a1 = browser.find_element(By.XPATH, '//*[@id="search-title"]')
a1.send_keys('евро') # пишем слово в поле которое можно заполнить
time.sleep(5)

button = browser.find_element(By.XPATH, '//*[@id="search"]')
button.click() # Нажать на кнопку

div1 = browser.find_element(By.XPATH, '//*[@id="donate"]/div')
div1 = div1.text

assert 'Просмотр доступен после доната любой суммы:' == div1
# закрываем браузер после всех манипуляций
time.sleep(20)
browser.quit()