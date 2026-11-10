#Использование нескольких сессий:
from playwright.sync_api import Page, BrowserContext
from pytest_playwright.pytest_playwright import CreateContextCallback

def test_foo(page: Page, new_context: CreateContextCallback) -> None:
    #открывает сайт
    page.goto("https://store.steampowered.com/")
    #context создает новую изолированную среду И В НЕЙ ОТКРЫВАЕТ НОВУЮ СТРАНИЧКУ
    context = new_context()
    page2 = context.new_page()

    # Для того, чтобы смоделировать нескольких пользователей


    #Медведева Дарья Сергеевна
    #09.11.2026
    #23:16