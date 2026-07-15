from playwright.sync_api import expect, Response, Request, sync_playwright
import pytest

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_disabled()

    registration_email = page.get_by_test_id("registration-form-email-input").locator("input")
    registration_email.fill("user.name@gmail.com")

    registration_username = page.get_by_test_id("registration-form-username-input").locator("input")
    registration_username.fill("username")

    registration_password = page.get_by_test_id("registration-form-password-input").locator("input")
    registration_password.fill("password")

    expect(registration_button).not_to_be_disabled()
    registration_button.click()

    context.storage_state(path="browser-state.json")

    page.wait_for_timeout(2000)


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    page.wait_for_timeout(2000)
