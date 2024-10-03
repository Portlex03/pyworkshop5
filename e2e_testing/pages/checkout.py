from playwright.sync_api import Page


class CheckoutInformationPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_name_field = page.locator("[data-test=\"firstName\"]")
        self.last_name_field = page.locator("[data-test=\"lastName\"]")
        self.postal_code =page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()


class CheckoutCompletePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.complete_header = page.locator("[data-test=\"complete-header\"]")


class CheckoutOverviewPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.finish_button = page.locator("[data-test=\"finish\"]")

    def click_finish_button(self) -> None:
        self.finish_button.click()
