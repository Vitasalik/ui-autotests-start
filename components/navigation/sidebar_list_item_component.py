from re import Pattern

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, indentifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f"{indentifier}-drawer-list-item-icon")
        self.title = page.get_by_test_id(f"{indentifier}-drawer-list-item-title-text")
        self.button = page.get_by_test_id(f"{indentifier}-drawer-list-item-button")

    def check_visible(self, title: str):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_visible(expected_url)

