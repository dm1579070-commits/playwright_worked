from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.screenshot(path="example.png")
    browser.close()

    #Медведева Дарья Сергеевна
        #10.11.2026
        #18:17
        #Без библиотеки pytest. Надо вручную расписывать действия программы.
        #Запускает выбранный браузер. Там создается вкладка.
        # В нашей папке появляется скрин страницы и браузер закрывается