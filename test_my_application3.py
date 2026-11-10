import pytest

#декоратор-условие, который говорит, что запускать можешь на всех браузерах, кроме Firefox
@pytest.mark.skip_browser("firefox")
def test_visit_example(page):    #тестовая функция
    #открывает сайт
    page.goto("https://store.steampowered.com/")


    #Медведева Дарья Сергеевна
    #10.11.2026
    #13:50