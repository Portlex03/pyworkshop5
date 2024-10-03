from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_list = page.get_by_role("listitem")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
