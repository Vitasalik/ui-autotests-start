import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page_with_state: CoursesListPage):
    courses_list_page_with_state.visible("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page_with_state.navbar.check_visible("username")
    courses_list_page_with_state.sidebar.check_visible()

    courses_list_page_with_state.toolbar_view.check_visible()
    courses_list_page_with_state.check_visible_empty_list()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page_with_state: CoursesListPage,
                       create_course_page_with_state: CreateCoursePage) -> None:
    create_course_page_with_state.visible(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    create_course_page_with_state.create_course_toolbar.check_visible(is_create_course_disabled=True)

    create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=False)

    create_course_page_with_state.create_course_form.check_visible("", "", "", "0", "0")

    create_course_page_with_state.create_course_exercises_toolbar.check_visible()
    create_course_page_with_state.check_visible_exercises_empty_view()

    create_course_page_with_state.image_upload_widget.upload_preview_image("./testdata/files/image.png")
    create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=True)

    create_course_page_with_state.create_course_form.fill_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10")
    create_course_page_with_state.create_course_toolbar.check_visible(is_create_course_disabled=False)
    create_course_page_with_state.create_course_toolbar.click_create_course_button()

    courses_list_page_with_state.toolbar_view.check_visible()
    courses_list_page_with_state.course_view.check_visible(
        0, "Playwright", "100", "10", "2 weeks")
