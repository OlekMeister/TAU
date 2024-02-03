from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Global WebDriver instance
driver = webdriver.Firefox()

@given('I open the Selenium documentation')
def step_open_selenium_documentation(context):
    context.driver = driver
    context.driver.get('https://selenium-python.readthedocs.io/index.html')
    context.driver.maximize_window()
    time.sleep(2)
    print("Test Passed")

@when('I maximize the window')
def step_maximize_window(context):
    context.driver.maximize_window()
    time.sleep(2)
    print("Test Passed")

@when('I click on the link firefox "{link_text}"')
def step_click_link(context, link_text):
    web = context.driver.find_element(by="link text", value=link_text)
    web.click()
    time.sleep(2)
    print("Test Passed")

@when('I scroll down the page')
def step_scroll_down(context):
    context.driver.execute_script("window.scrollTo(0, 600);")
    time.sleep(2)
    print("Test Passed")

@when('I scroll up the page')
def step_scroll_up(context):
    context.driver.execute_script("window.scrollTo(0, -400);")
    time.sleep(2)
    print("Test Passed")

@when('I go back to the main page')
def step_go_back_main_page(context):
    temp = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'logo')))
    temp.click()
    time.sleep(2)
    print("Test Passed")
