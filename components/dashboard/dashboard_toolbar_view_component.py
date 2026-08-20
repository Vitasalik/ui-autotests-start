import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar_title = Text(page,"dashboard-toolbar-title-text", "Title")

    @allure.step('Check visible dashboard toolbar view')
    def check_visible(self):
        self.toolbar_title.check_visible()
        self.toolbar_title.check_have_text("Dashboard")