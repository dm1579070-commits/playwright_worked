import os  #Для того, чтобы вытащить токен из настроек компьютера
from typing import Generator  #Для подсказок типов
import pytest        #Для тестирования
from playwright.sync_api import Playwright, APIRequestContext   #Для отправки запросов без браузера

#программа ищет токен в компьютере от github и кладет его в переменную. assert проверяет его наличие,
#  прежде чем запускать тесты
GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"

#декоратор фикструктуру запускает 1 раз и для всех тестов
@pytest.fixture(scope="session")

#сама фиструктура и там применяется Playwrigh
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    #словарь заголовок  с форматом и прикрепляется токен авторизации, чтобы github пускал запросы  
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_API_TOKEN}",
    }
    #объект для отправления запросов
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=headers
    )
    #пердаем готовые инструменты для запросов тестам и после завершения закрываем сессию и освобождаем ресурсы
    yield request_context
    request_context.dispose()

    #Медведева Дарья Сергеевна
    #12.11.2026
    #14:27
    # По сути код тестирует моего лица какой либо сайт. в моем случае от моего лица будет тестироваться github