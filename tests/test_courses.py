from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
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

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_toolbar = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_toolbar).to_be_visible()
        expect(courses_toolbar).to_have_text("Courses")

        courses_empty_list_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(courses_empty_list_icon).to_be_visible()

        courses_empty_list_title_text = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(courses_empty_list_title_text).to_be_visible()
        expect(courses_empty_list_title_text).to_have_text("There is no results")

        courses_empty_list_description_text = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(courses_empty_list_description_text).to_be_visible()
        expect(courses_empty_list_description_text).to_have_text(
            "Results from the load test pipeline will be displayed here")
