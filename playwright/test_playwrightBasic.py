from playwright.sync_api import Playwright, Page


# playwright param below is a fixture from pytest-playwright package.
def test_playwright_basic(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # like opening in incognito, once you exit, will reset session, cookies, etc
    page = context.new_page()
    page.goto("https://www.google.com")


# chromium headless mode, 1 single context
def test_playwright_shortcut(page: Page):
    page.goto("https://www.google.com")
