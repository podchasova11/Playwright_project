# import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo_3_3(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    # проверить что правильный адрес
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    # найти поле для ввода задач
    input_field = page.get_by_placeholder("What needs to be done?")
    # проверить что поле пустое
    expect(input_field).to_be_empty()
    # ввести первую задачу
    input_field.fill("First task")
    input_field.press("Enter")
    # ввести вторую задачу
    input_field.fill("Second task")
    input_field.press("Enter")
    # проверить кол-во задач в списке
    todo_item = page.get_by_test_id("todo-item")
    expect(todo_item).to_have_count(2)
    # отметить первую задачу как выполненную
    todo_item.get_by_role('checkbox').nth(0).click()
    # проверить что класс "выполнено"
    expect(todo_item.nth(0)).to_have_class("completed")
