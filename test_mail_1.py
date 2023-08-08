import pytest

@pytest.fixture()
def set_up():
    print('Вход в систему выполнен')
    yield
    print('Выход из системы')

def test_setting_mail_1(set_up):
    print('Письмо отправлено')

def test_setting_mail_2(set_up):
    print('Письмо отправлено')
from selenium import webdriver
driver = webdriver.chrome