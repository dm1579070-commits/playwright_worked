#код будет ждать, пока страница обнаружит заголовок, содержащий «Playwright»
import re
from playwright.sync_api import Page, expect

def test_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
  
  
    #Медведева Дарья Сергеевна
    #09.11.2026
    #17:27
