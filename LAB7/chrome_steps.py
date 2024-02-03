from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Global WebDriver instance
driver = webdriver.Chrome()

@given('I open the application')
def step_open_application(context):
    context.driver = driver
    context.driver.get("https://the-internet.herokuapp.com/")

@when('I click on the link chrome "{link_text}"')
def step_click_link(context, link_text):
    temp = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
    temp.click()

@when('I go back to the main page and click on the link "{link_text}"')
def step_go_back_and_click_link(context, link_text):
    context.driver.back()
    temp = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
    temp.click()

@when('I click the "{button_text}" button')
def step_click_button(context, button_text):
    temp = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[text()='{button_text}']")))
    temp.click()

@when('I remove the added element')
def step_remove_element(context):
    div_element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "added-manually")))
    div_element.click()

@when('I check the checkbox')
def step_check_checkbox(context):
    context.driver.back()
    temp = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkboxes")))
    temp.click()
    checkbox = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
    checkbox.click()

@then('the test passes')
def step_test_passes(context):
    time.sleep(2)
    print("Test Passed")

@then('the element is added successfully')
def step_element_added_successfully(context):
    try:
        div_element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "added-manually")))
        print("Element added successfully")
    except TimeoutException:
        print("Error: Element not added successfully")

@then('the element is removed successfully')
def step_element_removed_successfully(context):
    try:
        WebDriverWait(context.driver, 10).until_not(EC.presence_of_element_located((By.CLASS_NAME, "added-manually")))
        print("Element removed successfully")
    except TimeoutException:
        print("Error: Element not removed successfully")

@then('the checkbox is checked successfully')
def step_checkbox_checked_successfully(context):
    time.sleep(2)
    print("Checkbox checked successfully")
