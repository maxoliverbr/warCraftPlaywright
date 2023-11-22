import time

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

from utilities.testdata import TestData
from pages.basepage import BasePage


#@pytest.mark.parametrize("width,height", [(1920, 1080), (2560, 1080), (1366, 768)])
@pytest.mark.parametrize("width,height", [(1920, 1080)])
def test_login(playwright: Playwright, width, height):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(record_video_dir="reports/videos/")
    page = context.new_page()
    base_page = BasePage()


    # Test name: WarCraftLogin
    # Step # | name | target | value

    # 1 | open | /en-us/start |
    page.goto(TestData.url)

    # 2 | setWindowSize | width x height |
    page.set_viewport_size({"width": width, "height": height})

    # 6 | signup | start signup flow
    page.get_by_label("Account").click()
    page.get_by_role("link", name="Sign Up").click()

    # 7 | assert | confirm we are on the correct page
    expect(page.locator(base_page.signup_text_xpath)).to_have_text(base_page.signup_text)



    # 8 | birthdate | click continue without birthdate
    page.screenshot(path="screenshot.png", full_page=True)
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="Continue").click()

    # assert error message is correct
    expect(page.locator(base_page.error_text_xpath)).to_have_text(base_page.error_text_expected)

    # 9 | birthdate | enter birthdate mm/dd/yyyy
    page.get_by_placeholder("Date of Birth (mm / dd / yyyy)").click()
    page.fill(base_page.dob_month_xpath, "01")
    page.fill(base_page.dob_day_xpath, "01")
    page.fill(base_page.dob_year_xpath, "1970")


    # 10 | continue | click continue
    page.get_by_role("button", name="Continue").click()


    # 11 | user info | enter first & last name
    page.fill("#capture-first-name", TestData.user_first_name)
    page.fill("#capture-last-name", TestData.user_last_name)

    page.get_by_role("button", name="Continue").click()

    # 12 | user info part 2 | enter email and phone
    page.fill("#capture-email", TestData.user_email)
    page.fill("#capture-phone-number", TestData.user_phone)

    page.get_by_role("button", name="Continue").click()

    # 13 | assert step name
    #step_name = page.get_text(page.step_name_xpath)
    expect(page.locator(base_page.step_name_xpath)).to_have_text(base_page.step_name_expect)

    #assert step_name == page.step_name_expect

    #page.click(page.continue_id)

    # wait page load
    time.sleep(1)
    #page.save_screenshot('reports/ss/emailphone.png')

    # Make sure to close, so that videos are saved.
    context.close()
    browser.close()
