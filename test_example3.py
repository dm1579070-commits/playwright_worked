import pytest
from playwright.sync_api import Page, expect

#запускает перед каждым тестом заново и применять ко всем автоматически
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Переходите к начальному URL-адресу перед каждым тестом
    page.goto("https://playwright.dev/") #до теста: открыть сайт
    yield  # здесь бежит сам тест
    
    print("after the test runs")

def test_main_navigation(page: Page):
    # Утверждение использует ожидаемый API
    expect(page).to_have_url("https://playwright.dev/")