import pytest

@pytest.fixture(scope="session")  #Глобальная настройка. Подготовит один раз в самом начале, но для всех тестов сразу
def browser_context_args(browser_context_args):  #Переопределяет параметры
    return {
        **browser_context_args,
        "ignore_https_errors": True
    }

    #Медведева Дарья Сергеевна
    #10.11.2026
    #14:38
    #Игнорирует ошибки HTTPS (предупреждения безопасности)