from playwright.sync_api import Page

#Объявление теста с аргументом page, чтобы активировать нашу библиотеку
def test_visit_admin_dashboard(page: Page):
    #Открывает ссылку
    page.goto("https://www.python.org/")


    #Медведева Дарья Сергеевна
    #09.11.2026
    #23:16