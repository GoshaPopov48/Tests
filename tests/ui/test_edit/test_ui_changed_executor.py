from playwright.sync_api import sync_playwright, expect
from conftest import authenticated_page
import time

def test_changed_executor(authenticated_page):
    page = authenticated_page
    page.goto("http://localhost:8081/projects/DEMO/issues/DEMO-2/Pervye-shagi-polzovatelya")
    executor = page.locator('[data-test="field"]').filter(has=page.get_by_text("Исполнитель", exact=True)).get_by_role("combobox")
    
    executor.click()
    expect(executor).to_have_attribute("aria-expanded", "true")
    
    print(page.get_by_role("option").all_text_contents())
    
    new_executor = page.locator('[data-test="list-item-details"]').filter(has_text="Георгий Попов")
    new_executor.click()
    
    expect(executor).to_contain_text("Георгий Попов")
    page.reload()
    
    executor = page.locator('[data-test="field"]').filter(has=page.get_by_text("Исполнитель", exact=True)).get_by_role("combobox")
    expect(executor).to_contain_text("Георгий Попов")

    
