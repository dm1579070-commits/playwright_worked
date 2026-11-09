import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    #переходит по ссылке, чтобы начать тестирование
    page.goto("https://playwright.dev/")

    # Ожидается, что заголовок будет содержать строчку
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Нажмет ссылку «Начать»
    page.get_by_role("link", name="Get started").click()

    #Ожидается, что страница будет иметь заголовок с названием «Установка»
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


    #Медведева Дарья Сергеевна
    #09.11.2026
    #17:09
