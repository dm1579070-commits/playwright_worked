from playwright.sync_api import expect, Page

def test_foobar(page: Page) -> None:
    page.goto("https://store.steampowered.com/")
    #искуственно указываем тайм-аут
    expect(page.get_by_role("link", name="Магазин")).to_be_visible(timeout=10_000)