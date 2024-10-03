from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_list = page.get_by_role("listitem")
        self.backpack_locator = page.get_by_text("1Sauce Labs Backpackcarry.")
        self.tshirt_locator = page.get_by_text("1Sauce Labs Bolt T-ShirtGet")
        self.fleece_jacket_locator = page.get_by_text("1Sauce Labs Fleece JacketIt's")
