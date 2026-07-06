from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def check_current_url(self, expected_url: str) -> None:
        expect(self.page).to_have_url(expected_url)
