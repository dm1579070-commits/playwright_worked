#Скачиваются нужные библиотеки
from enum import auto
import os
from typing import Generator
import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

#программа ищет токен и юз в компьютере от github и кладет его в переменную. assert проверяет их наличие,
#  прежде чем запускать тесты
GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"
GITHUB_USER = os.getenv("GITHUB_USER")
assert GITHUB_USER, "GITHUB_USER is not set"
#задает название для репозитория, в котором будут тестироваться тесты
GITHUB_REPO = "test"

#Создается 1 сессия
@pytest.fixture(scope="session")
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

#Создается 1 сессия и для всех тестов автоматически
#создается репозиторий и проверяется его наличие. yield ставит программу на паузу и запускает тесты на баги. После
# удаляется репозиторий и проверяется его отсутствие
@pytest.fixture(scope="session", autouse=True)
def create_test_repository(
    api_request_context: APIRequestContext,
) -> Generator[None, None, None]:
    # Before all
    new_repo = api_request_context.post("/user/repos", data={"name": GITHUB_REPO})
    assert new_repo.ok
    yield
    # After all
    deleted_repo = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")
    assert deleted_repo.ok

#создается рапорт об ошибке. в словаре есть зпголовок и описание нашей проблемы
#делает запрос на новую задачу, беря проблему из нашего словаря
#проверяет действия теста повторно: сравнивает, проверяет корректность данных
def test_should_create_bug_report(api_request_context: APIRequestContext) -> None:
    data = {
        "title": "[Bug] report 1",
        "body": "Bug description",
    }
    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
    )
    assert new_issue.ok

    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok
    issues_response = issues.json()
    issue = list(
        filter(lambda issue: issue["title"] == "[Bug] report 1", issues_response)
    )[0]
    assert issue
    assert issue["body"] == "Bug description"

#создается тест на улучшения кода(проверки сообщений от пользователе). в словаре есть зпголовок и описание.
#создает\делает запрос на задачу
#проверяем, появилась ли задача и корректность ее данных
def test_should_create_feature_request(api_request_context: APIRequestContext) -> None:
    data = {
        "title": "[Feature] request 1",
        "body": "Feature description",
    }
    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
    )
    assert new_issue.ok

    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok
    issues_response = issues.json()
    issue = list(
        filter(lambda issue: issue["title"] == "[Feature] request 1", issues_response)
    )[0]
    assert issue
    assert issue["body"] == "Feature description"

    #Медведева Дарья Сергеевна
    #12.11.2026
    #23:27