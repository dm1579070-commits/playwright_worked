#библиотеки
from typing import Generator
from pathlib import Path
from playwright.sync_api import Playwright, BrowserContext
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

#фикструктура, которая задает нужные настройки. Заходит в браузер не под инкогнито и вбивает только наш плпгин, убирая другие
@pytest.fixture()
def context(playwright: Playwright) -> Generator[BrowserContext, None, None]:
    path_to_extension = Path(__file__).parent.joinpath("my-extension")
    context = playwright.chromium.launch_persistent_context(
        "",
        channel="chromium",
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )
    #пауза, фикструктура делает тесты
    yield context
    context.close()

#фикструктура, которая вычисляет ID плагина
@pytest.fixture()
def extension_id(context) -> Generator[str, None, None]:
    # фоновый скрипт плагина
    if len (context.service_workers) == 0:
        #вытаскивает из адреса ID
        service_worker = context.wait_for_event("serviceworker")
    else:
        service_worker = context.service_workers[0]
    #вытаскивает из адреса ID
    extension_id = service_worker.url.split("/")[2]
    #отдает этот ID тестам 
    yield extension_id

    #Медведева Дарья Сергеевна
    #14.11.2026
    #16:27



    #Медведева Дарья Сергеевна
    #10.11.2026
    #14:51
    #пользовательский размер области просмотра. Принудительно задает размер окна
    # и игнорирует ошибки HTTPS (предупреждения безопасности)