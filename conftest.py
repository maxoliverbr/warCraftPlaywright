import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from utilities.testdata import TestData

"""
Fixture to open the browser instance for each test case.
"""


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(playwright: Playwright, request):
    if request.param == "chrome":
        chromium = playwright.chromium
        browser = chromium.launch()

    elif request.param == "firefox":
        chromium = playwright.chromium
        browser = chromium.launch()

    elif request.param == "edge":
        chromium = playwright.chromium
        browser = chromium.launch()

    page = browser.new_page()
    request.cls.driver = page
    yield
    browser.close()
