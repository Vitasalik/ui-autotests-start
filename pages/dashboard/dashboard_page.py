import re

from playwright.sync_api import Page

from components.charts.chart_view_copmponent import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from tools.routes import AppRoute


class DashboardPage(BasePage):
    URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"

    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

        self.students_chart = ChartViewComponent(page, "students", "bar")
        self.courses_chart = ChartViewComponent(page, "courses", "pie")
        self.scores_chart = ChartViewComponent(page, "scores", "scatter")
        self.activities_chart = ChartViewComponent(page, "activities", "line")

    def check_opened(self):
        self.check_current_url(re.compile(AppRoute.DASHBOARD))

