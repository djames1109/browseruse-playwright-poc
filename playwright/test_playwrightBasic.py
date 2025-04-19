

# playwright param below is a fixture from pytest-playwright package.
def test_playwright_basic(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # like opening in incognito, once you exit, will reset session, cookies, etc
    page = context.new_page()
    page.goto("https://www.google.com")