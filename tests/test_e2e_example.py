import pytest
from playwright.sync_api import sync_playwright, Page

def access_website(page: Page, url: str):
    page.goto(url)

def enter_number_in_first_field(page: Page, number: str):
    page.fill('#sum1', number)

def enter_number_in_second_field(page: Page, number: str):
    page.fill('#sum2', number)

def click_button(page: Page, button_text: str):
    page.click(f'//button[contains(text(), "{button_text}")]')

def check_result(page: Page, expected_result: str):
    result = page.inner_text('#addmessage')
    assert result == expected_result

@pytest.fixture(scope='session')
def browser_context():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()
    playwright.stop()

@pytest.fixture(scope='function')
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()

def test_sum_form(page: Page):
    test_cases = [
        {'first_number': '5', 'second_number': '10', 'expected_result': '15'},
        {'first_number': '3', 'second_number': '7', 'expected_result': '10'},
        {'first_number': '1', 'second_number': '1', 'expected_result': '2'},
        {'first_number': '13', 'second_number': '1', 'expected_result': '14'},
        {'first_number': '999', 'second_number': '1', 'expected_result': '1000'},
    ]

    for test_case in test_cases:
        # Access the website
        access_website(page, 'https://www.lambdatest.com/selenium-playground/simple-form-demo')

        # Enter numbers and click the button
        enter_number_in_first_field(page, test_case['first_number'])
        enter_number_in_second_field(page, test_case['second_number'])
        click_button(page, 'Get Sum')

        # Check the result
        check_result(page, test_case['expected_result'])
