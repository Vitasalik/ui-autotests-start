import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id("registration-page-registration-button")

    registration_email = page.get_by_test_id("registration-form-email-input").locator("input")
    registration_email.fill("user.name@gmail.com")

    registration_username = page.get_by_test_id("registration-form-username-input").locator("input")
    registration_username.fill("username")

    registration_password = page.get_by_test_id("registration-form-password-input").locator("input")
    registration_password.fill("password")

    registration_button.click()

    context.storage_state(path="browser-state.json")
    browser.close()

@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close(),