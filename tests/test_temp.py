from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://worldofwarcraft.blizzard.com/en-us/start")
    page.get_by_label("Account").click()
    page.get_by_role("link", name="Sign Up").click()
