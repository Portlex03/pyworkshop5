from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.backpack_button = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.tshirt_button = page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.fleece_jacket_button = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")

    def add_items_to_shopping_cart(self):
        self.backpack_button.click()
        self.tshirt_button.click()
        self.fleece_jacket_button.click()
