import os

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from ..pages.login import LoginPage


def test_login_with_incorrect_data(page: Page) -> None:
    load_dotenv()
    site_url = os.getenv("SITE_URL")
    username = os.getenv("USER_LOGIN")
    password = os.getenv("USER_PASSWORD_WRONG")

    login_page = LoginPage(page)
    login_page.navigate(site_url)
    login_page.enter_username(username)
    login_page.enter_password(password)

    message = "Epic sadface: Username and password \
        do not match any user in this service"
    expect(login_page.error_field, message)
