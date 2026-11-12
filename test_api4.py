from playwright.sync_api import Playwright, Page, APIRequestContext, expect
import os
GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"
GITHUB_USER = os.getenv("GITHUB_USER")
assert GITHUB_USER, "GITHUB_USER is not set"
#задает название для репозитория, в котором будут тестироваться тесты
GITHUB_REPO = "test"


def test_last_created_issue_should_be_first_in_the_list(api_request_context: APIRequestContext, page: Page) -> None:
    #Принимает заголовок, формирует данные и создает задачу на github. без открытия браузера
    def create_issue(title: str) -> None:
        data = {
            "title": title,
            "body": "Feature description",
        }
        new_issue = api_request_context.post(
            f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
        )
        assert new_issue.ok

    #вызываем функцию и в репозитории test будут лежать две новые задачи
    create_issue("[Feature] request 1")
    create_issue("[Feature] request 2")
    #открывает в браузере страничку репозитория на Гидхаб с issues
    page.goto(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues")
    #проверка в браузере. Ищем на страничке задачи и берем первую
    first_issue = page.locator("a[data-hovercard-type='issue']").first
    expect(first_issue).to_have_text("[Feature] request 2")