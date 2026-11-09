import pytest

@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...

    #Медведева Дарья Сергеевна
    #09.11.2026
    #23:16