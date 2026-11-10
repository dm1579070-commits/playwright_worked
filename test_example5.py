import pytest
from playwright.async_api import Page

@pytest.mark.asyncio(loop_scope="session")
async def test_foo(page: Page):
    await page.goto("https://github.com")
    #Медведева Дарья Сергеевна
    #09.11.2026
    #15:20
    #Асинхронный стиль кода. В декораторе запускается собыйтийный цикл 1 раз на всю сессию.
    #Дальше обЪявления асинхр. функции и await - это запускает сайт, но програму не блокирует, а ждет, делая другие задачи
