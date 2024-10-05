from playwright.sync_api import Page, expect

from ..pages.login import LoginPage


def test_login_with_incorrect_data(page: Page) -> None:
    site_url = "https://www.saucedemo.com"
    username = "standard_user"
    password = "wrong_password"

    login_page = LoginPage(page)
    login_page.navigate(site_url)
    login_page.login(username, password)

    message = "Epic sadface: Username and password \
        do not match any user in this service"
    expect(login_page.error_field, message)
