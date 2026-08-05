import pytest
from playwright.sync_api import expect, Page

from pages.dashboard_page import DashboardPage

@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visible("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page_with_state.navbar.check_visible("username")
    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.check_visible_toolbar_title()
    dashboard_page_with_state.check_visible_students()
    dashboard_page_with_state.check_visible_courses()
    dashboard_page_with_state.check_visible_activities()
    dashboard_page_with_state.check_visible_scores()
