import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # Подключаем библиотеку для работы со списком

link = "https://www.provartesting.com/contact/?utm_source=google&utm_medium=cpc&utm_campaign=uk_competitor&gclid=Cj0KCQjwz8emBhDrARIsANNJjS5nGD0ripp8PE5713StPCS5Ay_rdYqVyo6yxC6-LmVHKhwc618lwqwaAoOeEALw_wcB" # (меняем название сайта(в поисковой строке)
browser = webdriver.Chrome()
browser.get(link)

select1 = Select(browser.find_element(By.XPATH, '//*[@id="input_11_10"]')) #Находим список (раскрывающийся)
select1.select_by_value("Austria") #Выбираем нужный эллемент списка

time.sleep(20)
browser.quit()