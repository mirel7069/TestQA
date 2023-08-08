import pytest

@pytest.fixture()
def set_up():
    print('Вход в систему выполнен')
    yield
    print('выход из системы')

def test_setting_mail_1():
    print('Письмо отправлено')

def test_setting_mail_2():
    print('Письмо отправлено')
