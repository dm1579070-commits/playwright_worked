import pytest
#Глобальная настройка. Подготовит один раз в самом начале, но для всех тестов сразу
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):  #Переопределяет параметры
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "ignore_https_errors": True
    }

    #Медведева Дарья Сергеевна
    #10.11.2026
    #14:51
    #пользовательский размер области просмотра. Принудительно задает размер окна
    # и игнорирует ошибки HTTPS (предупреждения безопасности)