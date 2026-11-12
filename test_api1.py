import os
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

#программа ищет токен в компьютере от github и кладет его в переменную. assert проверяет его наличие,
#  прежде чем запускать тесты
GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"

#программа ищет юз в компьютере от github и кладет его в переменную. assert проверяет его наличие юзера,
#  прежде чем запускать тесты
GITHUB_USER = os.getenv("GITHUB_USER")
assert GITHUB_USER, "GITHUB_USER is not set"

#задает имя репозитория и там будут происходить все действия
GITHUB_REPO = "test"

#создается рапорт об ошибке. в словаре есть зпголовок и описание нашей проблемы
def test_should_create_bug_report(api_request_context: APIRequestContext) -> None:
    data = {
        "title": "[Bug] report 1",
        "body": "Bug description",
    }
    #создает\делает запрос на новую задачу, беря проблему из нашего словаря
    new_issue = api_request_context.post(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data)
    assert new_issue.ok

    #проверяет действия теста повторно: сравнивает, проверяет корректность данных
    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok
    issues_response = issues.json()
    issue = list(filter(lambda issue: issue["title"] == "[Bug] report 1", issues_response))[0]
    assert issue
    assert issue["body"] == "Bug description"

#создается запрос на улучшения кода. в словаре есть зпголовок и описание
def test_should_create_feature_request(api_request_context: APIRequestContext) -> None:
    data = {
        "title": "[Feature] request 1",
        "body": "Feature description",
    }
    #создает\делает запрос на задачу
    new_issue = api_request_context.post(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data)
    assert new_issue.ok
    #проверяем, появилась ли задача и корректность ее данных
    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok
    issues_response = issues.json()
    issue = list(filter(lambda issue: issue["title"] == "[Feature] request 1", issues_response))[0]
    assert issue
    assert issue["body"] == "Feature description"

    #Медведева Дарья Сергеевна
    #12.11.2026
    #14:37