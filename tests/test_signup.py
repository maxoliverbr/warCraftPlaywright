import time

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

from utilities.testdata import TestData
from pages.basepage import BasePage


#@pytest.mark.parametrize("width,height", [(1920, 1080), (2560, 1080), (1366, 768)])
@pytest.mark.parametrize("width,height", [(1920, 1080)])
def test_login(playwright: Playwright, width, height):
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
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
    #page.click(page.bird_date_xpath)

    #error_text = page.get_text(page.error_text_xpath)

    # assert error message is correct
    #assert error_text == page.error_text_expected
    #page.click(page.dob_xpath)

    # 9 | birthdate | enter birthdate mm/dd/yyyy
    #page.set(page.dob_month_xpath, TestData.dob_mon)
    #page.set(page.dob_day_xpath, TestData.dob_day)
    #page.set(page.dob_year_xpath, TestData.dob_year)

    # 10 | continue | click continue
    #page.click(page.continue_id)
    #page.save_screenshot('reports/ss/continue.png')

    # 11 | user info | enter first & last name
    #page.set(page.first_name_id, TestData.user_first_name)
    #page.set(page.last_name_id, TestData.user_last_name)
    #page.save_screenshot('reports/ss/last.png')

    #page.click(page.continue_id)

    # 12 | user info part 2 | enter email and phone
    #page.set(page.email_id, TestData.user_email)
    #page.set(page.phone_id, TestData.user_phone)

    #page.click(page.continue_id)

    # 13 | assert step name
    #step_name = page.get_text(page.step_name_xpath)

    #assert step_name == page.step_name_expect

    #page.click(page.continue_id)

    # wait page load
    time.sleep(1)
    #page.save_screenshot('reports/ss/emailphone.png')

    # Make sure to close, so that videos are saved.
    context.close()
    browser.close()
