""" POM BasePage """


class BasePage:
    """
    BasePage contains methods common to all Page Objects
    """
    shadow_root_0_css = ".SiteNav"
    shadow_root_1_css = "#blz-nav-sign-up"
    signup_id = "blz-nav-sign-up"
    jsclick = "arguments[0].click();"

    signup_text_xpath = "//h1[@class='step__title step__block']"
    signup_text = "Sign Up With"

    bird_date_xpath = "//button[@class='step__button step__button--primary']"

    error_text_xpath = "//li[@class='step__field-errors-item']"
    error_text_expected = "Your date of birth is required"

    dob_xpath = "//*[@name='dob-plain']"

    dob_month_xpath = "//input[@name='dob-month']"
    dob_day_xpath = "//input[@name='dob-day']"
    dob_year_xpath = "//input[@name='dob-year']"

    continue_id = "flow-form-submit-btn"

    first_name_id = "capture-first-name"
    last_name_id = "capture-last-name"

    email_id = "capture-email"
    phone_id = "capture-phone-number"
    step_name_xpath = "//h1[@class='step__title step__block']"
    step_name_expect = 'Identify Your Account'

    # def __init__(self, driver):
    #     self.driver = driver
    #
    # def load(self, url):
    #     self.driver.get(url)
    #
    # def find(self, *locator):
    #     return self.driver.find_element(*locator)
    #
    # def click(self, locator):
    #     return self.find(*locator).click()
    #
    # def set(self, locator, value):
    #     # click() necessary for Firefox
    #     self.find(*locator).click()
    #     self.find(*locator).clear()
    #     self.find(*locator).send_keys(value)
    #
    # def get_text(self, locator):
    #     return self.find(*locator).text
    #
    # def get_title(self):
    #     return self.driver.title
    #
    # def set_size(self, x, y):
    #     self.driver.set_window_size(x, y)
    #
    # def get_shadow(self, selector):
    #     return self.driver.find_element(*selector).shadow_root
    #
    # @staticmethod
    # def get_nested_shadow(dom, selector):
    #     return dom.find_element(*selector).shadow_root
    #
    # def save_screenshot(self, path):
    #     self.driver.save_screenshot(path)
