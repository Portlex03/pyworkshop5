from playwright.sync_api import Page, expect

from ..pages.cart import CartPage
from ..pages.checkout import CheckoutCompletePage, CheckoutInformationPage, CheckoutOverviewPage
from ..pages.inventory import InventoryPage
from ..pages.login import LoginPage


def test_successful_making_order(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_items_to_shopping_cart()
    inventory_page.shopping_cart_link.click()

    cart_page = CartPage(page)
    cart_page.checkout_button.click()

    checkout_information = CheckoutInformationPage(page)
    checkout_information.fill_checkout_info("Andrey", "Maybah", "1234")

    checkout_overview = CheckoutOverviewPage(page)
    checkout_overview.click_finish_button()

    checkout_complete = CheckoutCompletePage(page)
    expect(checkout_complete.complete_header).to_have_text("Thank you for your order!")
