from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_field = page.locator('[data-test="username"]')
        self.password_field = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_field = page.locator('[data-test="error"]')

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def login(self, username: str, password: str) -> None:
        self.login_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
