import pytest
import allure
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page_with_state: CoursesListPage):
        courses_list_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page_with_state.navbar.check_visible("username")
        courses_list_page_with_state.sidebar.check_visible()

        courses_list_page_with_state.toolbar_view.check_visible()
        courses_list_page_with_state.check_visible_empty_list()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page_with_state: CoursesListPage,
                           create_course_page_with_state: CreateCoursePage) -> None:
        create_course_page_with_state.visit(
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
            min_score="10"
        )
        create_course_page_with_state.create_course_toolbar.check_visible(is_create_course_disabled=False)
        create_course_page_with_state.create_course_toolbar.click_create_course_button()

        courses_list_page_with_state.toolbar_view.check_visible()
        courses_list_page_with_state.course_view.check_visible(
            0, "Playwright", "100", "10", "2 weeks")

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page_with_state: CreateCoursePage, courses_list_page_with_state: CoursesListPage):
        create_course_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page_with_state.create_course_form.fill_form(
            title="Java",
            estimated_time="10 weeks",
            description="Java",
            max_score="200",
            min_score="30"
        )
        create_course_page_with_state.image_upload_widget.upload_preview_image("./testdata/files/java.png")
        create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page_with_state.create_course_toolbar.click_create_course_button()

        courses_list_page_with_state.toolbar_view.check_visible()
        courses_list_page_with_state.course_view.check_visible(
            index=0, title="Java", max_score="200", min_score="30", estimate_time="10 weeks"
        )
        courses_list_page_with_state.course_view.menu.click_edit(index=0)

        create_course_page_with_state.create_course_form.fill_form(
            title="Python",
            estimated_time="20 weeks",
            description="Python",
            max_score="100",
            min_score="20"
        )
        create_course_page_with_state.image_upload_widget.upload_preview_image("./testdata/files/python.png")
        create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page_with_state.create_course_toolbar.click_create_course_button()

        courses_list_page_with_state.toolbar_view.check_visible()
        courses_list_page_with_state.course_view.check_visible(
            index=0, title="Python", estimate_time="20 weeks", max_score="100", min_score="20"
        )

