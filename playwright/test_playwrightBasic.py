import time

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


def test_core_locators(playwright):
    page:Page = get_headed_browser(playwright).new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy") # only works if the label is associated with the text box using 'for'.
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check() # CSS locator. this one selects the checkbox and mark it as checked
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)


def get_headed_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    return context
