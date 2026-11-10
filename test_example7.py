from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://store.steampowered.com/")
page.screenshot(path="example.png")
browser.close()
playwright.stop()


#Медведева Дарья Сергеевна
    #10.11.2026
    #18:12
    #Тоже самое. вручную расписываем что будет делать библиотека, но вместо
    #вывода в терминале будет скриншот
    