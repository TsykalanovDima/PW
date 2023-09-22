import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com")
    us_name = page.locator("[placeholder='Username']")
    us_name.fill('standard_user')
    password = page.locator("[type='password']")
    password.fill('secret_sauce')
    page.locator("[class='submit-button btn_action']").click()
    app_logo = page.locator(".app_logo")
    expect(app_logo).to_have_text("Swag Labs")
    page.locator("#item_4_title_link").click()
    check = page.locator("[class ='inventory_details_name large_size']")
    expect(check).to_have_text('Sauce Labs Backpack')
    page.locator('[name="back-to-products"]').click()
    expect(app_logo).to_have_text("Swag Labs")
    page.locator('#react-burger-menu-btn').click()
    page.locator('#logout_sidebar_link').click()
    expect(us_name).to_be_empty()
    expect(password).to_be_empty()

    time.sleep(3)
    browser.close()
