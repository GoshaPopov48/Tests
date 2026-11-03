from playwright.sync_api import Page

class LoginPage:
    
    def __init__(self, page: Page):
        self.page = page
        
        self.username = page.locator('[data-test="username-field"]')
        self.password = page.locator('[data-test="password-field"]')
        self.remember_me = page.locator('[data-test="ring-checkbox"]')
        self.login_button = page.locator('[data-test="login-button"]')
        
    def enter_username(self, username : str):
        self.username.fill(username)
    
    def enter_password(self, password: str):
        self.password.fill(password)

    def set_remember_me(self, checked: bool):
        if checked:
            self.remember_me.check()
        else:
            self.remember_me.uncheck()

    def click_login(self):
        self.login_button.click()
    
    
    def login(self, username : str, password : str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()