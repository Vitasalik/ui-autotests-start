from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"

    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar_title = page.get_by_test_id("dashboard-toolbar-title-text")

        self.students_title = page.get_by_test_id("students-widget-title-text")
        self.students_chart = page.get_by_test_id("students-bar-chart")

        self.activities_title = page.get_by_test_id("activities-widget-title-text")
        self.activities_chart = page.get_by_test_id("activities-line-chart")

        self.courses_title = page.get_by_test_id("courses-widget-title-text")
        self.courses_chart = page.get_by_test_id("courses-pie-chart")

        self.scores_title = page.get_by_test_id("scores-widget-title-text")
        self.scores_chart = page.get_by_test_id("scores-scatter-chart")

    def check_opened(self) -> None:
        self.check_current_url(self.URL)

    def check_visible_toolbar_title(self) -> None:
        expect(self.toolbar_title).to_be_visible()
        expect(self.toolbar_title).to_have_text("Dashboard")

    def check_visible_students(self) -> None:
        expect(self.students_title).to_be_visible()
        expect(self.students_title).to_have_text("Students")
        expect(self.students_chart).to_be_visible()

    def check_visible_courses(self) -> None:
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text("Courses")
        expect(self.courses_chart).to_be_visible()

    def check_visible_scores(self) -> None:
        expect(self.scores_title).to_be_visible()
        expect(self.scores_title).to_have_text("Scores")
        expect(self.scores_chart).to_be_visible()

    def check_visible_activities(self) -> None:
        expect(self.activities_title).to_be_visible()
        expect(self.activities_title).to_have_text("Activities")
        expect(self.activities_chart).to_be_visible()
