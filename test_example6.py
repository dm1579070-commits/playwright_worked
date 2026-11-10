from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://store.steampowered.com/")
    print(page.title())
    browser.close()


    #Медведева Дарья Сергеевна
    #09.11.2026
    #17:15
    #Без библиотеки pytest. Надо вручную расписывать действия программы.
    #Запускает выбранный браузер. Там создается вкладка.
    # В терминале появляется заголовок страницы и браузер закрывается