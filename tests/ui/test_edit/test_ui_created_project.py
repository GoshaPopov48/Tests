from playwright.sync_api import sync_playwright, expect
from conftest import authenticated_page
import time
import uuid


def  test_created_project(authenticated_page):
    suffix = uuid.uuid4().hex[:3]
    page = authenticated_page
    
    page.goto("http://localhost:8081/projects")

    page.get_by_role("link", name="Новый проект").click()
    
    template = page.get_by_role("button", name="Управление задачами Упрощенный проект для повседневного управления задачами")
    
    expect(template).to_be_visible()
    template.click()
    page.get_by_role("button", name="Использовать шаблон").click()
    page.get_by_placeholder("Введите имя проекта").fill(f"Test_{suffix}")
    page.locator('[data-test="project-id"]').fill(f"sdf_{suffix}")
    page.get_by_role("button", name="Создать проект").click()
    temp = page.get_by_role("button", name="Пропустить настройку и перейти к проекту")
    expect(temp).to_be_visible()
    temp.click()
    print("Проект создан")