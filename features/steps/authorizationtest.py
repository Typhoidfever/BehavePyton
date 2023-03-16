from behave import *
from selenium import webdriver
from POM.main_page import Mainpage
from POM.login_page import Loginpage

use_step_matcher("re")

login = "miyile8564@otanhome.com"
password = "Pass@word1"


@given("I am navigate to website")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    page = Mainpage(context.driver)
    context.page = page
    context.page.open_page()


@when("Click Log in button")
def step_impl(context):
    context.page.click_sign_in()


@when("Enter my creds")
def step_impl(context):
    context.login_page = Loginpage(context.driver)
    context.login_page.perform_authorization(login, password)


@step("Click Authorization button")
def step_impl(context):
    context.login_page.click_login()


@then("I successfully authorized on website")
def step_impl(context):
    context.page.sign_out_is_present()
