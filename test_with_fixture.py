import re
from playwright.sync_api import Playwright, sync_playwright, expect

# имитация фикстуры page
# @pytest.fixture
# def browser_fixture():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         page.close()
#         browser.close()


def test_add_todo_tasko(page):

    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
