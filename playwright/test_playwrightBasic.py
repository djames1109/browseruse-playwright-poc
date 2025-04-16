from playwright.sync_api import Playwright


def test_playwright_basic(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")


# headless chromium,
def test_playwright_shortcut(page):
    page.goto("https://www.google.com/")