import pytest
#декоратор-условие, который говорит, что этот тест нельзя запускатьна всех браузерах, кроме chromium
@pytest.mark.only_browser("chromium")  
def test_visit_example(page):           #тестовая функция
    page.goto("https://example.com")    #открывает сайт



    #Медведева Дарья Сергеевна
    #10.11.2026
    #14:02