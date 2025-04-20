import time

from playwright.sync_api import Page, expect, Playwright


def test_hideShowUIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


def test_alertBox(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # when pop up appears, click on ok.
    page.on("popup", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()  # this makes the dialog popup box to appear
    time.sleep(5)
