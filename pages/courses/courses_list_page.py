import pytest
from playwright.sync_api import Page, expect

from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Горизонтальный navbar
        self.navbar = NavbarComponent(page)

        # Вертикальный sidebar
        self.sidebar = SidebarComponent(page)

        # Пустой блок при отсутствии курсов
        self.empty_view = EmptyViewComponent(page, "courses-list")

        # Заголовок и кнопка создания курса
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # Карточка курса
        self.course_view = CourseViewComponent(page)


    def check_visible_empty_list(self) -> None:
        self.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here"
        )


