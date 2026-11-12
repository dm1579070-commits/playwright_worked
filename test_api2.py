import os
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

#программа ищет юз в компьютере от github и кладет его в переменную. assert проверяет его наличие юзера,
#  прежде чем запускать тесты
GITHUB_USER = os.getenv("GITHUB_USER")
assert GITHUB_USER, "GITHUB_USER is not set"
#задает название для репозитория, в котором будут тестироваться тесты
GITHUB_REPO = "test"
#Создается 1 сессия и для всех тестов автоматически
@pytest.fixture(scope="session", autouse=True)
#Создается репозиторий для тестирования тестов
def create_test_repository(
    api_request_context: APIRequestContext,
) -> Generator[None, None, None]:
    # создается репозиторий и проверяется его наличие. yield ставит программу на паузу и запускает тесты на баги допустим
    new_repo = api_request_context.post("/user/repos", data={"name": GITHUB_REPO})
    assert new_repo.ok
    yield
    # удаляется репозиторий и проверяется его отсутствие
    deleted_repo = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")
    assert deleted_repo.ok