from playwright.sync_api import Page, expect

from ..pages.login import LoginPage
from ..pages.inventory import InventoryPage
from ..pages.cart import CartPage


def test_adding_several_items_to_shopping_cart(page: Page) -> None:
    site_url = "https://www.saucedemo.com"
    username = "standard_user"
    password = "secret_sauce"

    login_page = LoginPage(page)
    login_page.navigate(site_url)
    login_page.login(username, password)

    inventory_page = InventoryPage(page)
    inventory_page.add_items_to_shopping_cart()
    inventory_page.shopping_cart_link.click()

    cart_page = CartPage(page)
    expect(cart_page.cart_list).to_have_count(3)
