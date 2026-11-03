import pytest
from playwright.sync_api import sync_playwright
from tests.ui.pages.login_schemas import LoginPage

@pytest.mark.parametrize(
    "username, password",
    [
        ("Gosha", "admin")
    ]
)
def test_auth(username, password):
    with sync_playwright() as pl:
        browser = pl.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("http://localhost:8081/hub/auth/login")
        login_page = LoginPage(page)
        login_page.login(username, password)
        
        
        assert page.goto("http://localhost:8081/dashboard?id=173-0")
        print("Авторизация успешна")
        
        browser.close()