import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://kursk.pgups.ru/" # (меняем название сайта(в поисковой строке)
browser = webdriver.Chrome()
browser.get(link)


button = browser.find_element(By.XPATH, '//*[@id="menu-item-736"]/a')
button.click() # Нажать на кнопку

div1 = browser.find_element(By.XPATH, '//*[@id="menu-item-8754"]/a')
div1 = div1.text

assert 'Обратная связь' == div1 # УТВЕРЖДАЕМ!(сравниваем) слово после нажатия кнопки
# закрываем браузер после всех манипуляций
time.sleep(20)
browser.quit()