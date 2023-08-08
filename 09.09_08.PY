import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://jeogame.narod.ru/index.html" # (меняем название сайта(в поисковой строке)
browser = webdriver.Chrome()
browser.get(link)


button = browser.find_element(By.XPATH, '//*[@id="layout"]/tbody/tr[2]/td[1]/a[1]')
button.click() # Нажать на кнопку

div1 = browser.find_element(By.XPATH, '//*[@id="layout"]/tbody/tr[2]/td[2]/h1[1]')
div1 = div1.text

assert 'Добро пожаловать на сайт Компьютерной версии "Своей игры"!' == div1 # УТВЕРЖДАЕМ!(сравниваем) слово после нажатия кнопки
# закрываем браузер после всех манипуляций
time.sleep(20)
browser.quit()