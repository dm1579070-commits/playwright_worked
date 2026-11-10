import pytest

#декоратор-условие, который говорит, что запускать можешь на всех браузерах, кроме webkit
@pytest.mark.skip_browser("webkit")
def test_visit_example(page):    #тестовая функция
    #открывает сайт
    page.goto("https://store.steampowered.com/")


    #Медведева Дарья Сергеевна
    #10.11.2026
    #13:50