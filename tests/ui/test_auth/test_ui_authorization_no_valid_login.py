import pytest
from uuid import uuid4
from playwright.sync_api import sync_playwright, expect
from tests.ui.pages.login_schemas import LoginPage


@pytest.mark.parametrize(
    "username, password, expect_result",
    [ 
    ("goshass", "admin", "error"),
    (" ", "admin", "error"),
    ("1234124fds", "admin", "error"),
    ]
)
def test_no_valid_login_auth(username, password, expect_result):
    
    with sync_playwright() as pl:
        browser = pl.chromium.launch(headless=False)
        page = browser.new_page()
        suffix = uuid4().hex[:6]
        try:
            page.goto("http://localhost:8081/hub/auth/login")
            login_page = LoginPage(page)
            login_page.login(username, password)
            
            if expect_result == "error":
                expect(
                        page.locator('[data-test="username-field"]')
                    ).to_be_visible()
                print("Ошибка авторизации, проверьте логин")
                page.screenshot(path=f"screenshots/error_auth/NovalidUsername/Test_{suffix}.png")
            
        finally:
                browser.close()
            
        