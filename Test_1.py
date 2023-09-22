<<<<<<< HEAD
import time

=======
>>>>>>> 767ef5d573308be983d78e99064c541956478256
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com")
    page.locator("[placeholder='Username']").fill('standard_user')
    page.locator("[type='password']").fill('secret_sauce')
    page.locator("[class='submit-button btn_action']").click()
    app_logo = page.locator(".app_logo")
    try:
        expect(app_logo).to_have_text("Swag Labs")
        print("\nOkey")
    except:
        print("\nNo")

    page.locator("[name='add-to-cart-sauce-labs-backpack']").click()
    shop_card = page.locator(".shopping_cart_badge")
    badge_text = shop_card.text_content()

<<<<<<< HEAD
=======
    # Проверить, что текст равен "1"
>>>>>>> 767ef5d573308be983d78e99064c541956478256
    if badge_text == "1":
        print("1 item")
    else:
        print("0 item")

    page.select_option("[class='product_sort_container']", "Price (low to high)")

<<<<<<< HEAD
    browser.close()
=======
    page.wait_for_timeout(2000)
>>>>>>> 767ef5d573308be983d78e99064c541956478256





