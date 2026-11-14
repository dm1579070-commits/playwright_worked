from playwright.sync_api import expect, Page

#вызываю фикструктуры их confitest1.py. Тест переходит на сайт и проверяет, что плагин успешно внедрен и сайт изменен
def test_example_test(page: Page) -> None:
    page.goto("https://example.com")
    expect(page.locator("body")).to_contain_text("Changed by my-extension")

#переходит в САМ ПЛАГИН.И смотрим тег body, проверяя написание теста.
def test_popup_page(page: Page, extension_id: str) -> None:
    page.goto(f"chrome-extension://{extension_id}/popup.html")
    expect(page.locator("body")).to_have_text("my-extension popup")


        #Медведева Дарья Сергеевна
    #14.11.2026
    #17:27