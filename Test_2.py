import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com")
    page.locator("[placeholder='Username']").fill('problem_user')
    page.locator("[type='password']").fill('secret_sauce')
    page.locator("[class='submit-button btn_action']").click()
    check = page.locator("[class='title']")
    expect(check).to_have_text("Products")
    div_count = page.eval_on_selector_all(
        '.inventory_list .inventory_item',
        '(elements) => elements.length'
    )
    if div_count == 6:
        print('\nWork')
    else:print("\nDoesnt work")

    img_elements = page.locator('.inventory_item_img').all()
    unique_urls = set()
    for img in img_elements:
        img_url = img.get_attribute('src')
        if img_url is not None:
            if img_url in unique_urls:
                print(f"Дублирующийся URL-адрес: {img_url}")
            else:
                unique_urls.add(img_url)

    if len(unique_urls) == len(img_elements):
        print("Все картинки уникальны.")
    else:
        print("Есть дублирующиеся картинки.")


    time.sleep(3)
    browser.close()



