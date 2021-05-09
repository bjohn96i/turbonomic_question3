import sys
import pytest
import random
from pageObjects.mainPage.locators import Locator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.headless = False
service = Service('chrome_webdriver\\chromedriver.exe')
browser = webdriver.Chrome(options=options, service=service)

def test_validate_dropdown():
    selection1 = random.randint(1,10)
    selection2 = random.randint(11,20)
    browser.get('https://sanusart.github.io/react-dropdown-select/')
    browser.find_element(By.CSS_SELECTOR, Locator.clear_btn).click()
    browser.find_element(By.CSS_SELECTOR, Locator.main_dropdown).click()

    browser.find_element(By.CSS_SELECTOR, Locator.dropdown_menu+f':nth-of-type({selection1})').click()
    name = browser.find_element(By.CSS_SELECTOR, Locator.dropdown_menu+f':nth-of-type({selection1})').text
    assert name == (browser.find_element(By.CSS_SELECTOR, Locator.dropdown_selection).text).replace('\n×', '')
    
    browser.find_element(By.CSS_SELECTOR, Locator.dropdown_menu+f':nth-of-type({selection2})').click()
    name = browser.find_element(By.CSS_SELECTOR, Locator.dropdown_menu+f':nth-of-type({selection2})').text
    assert name == (browser.find_element(By.CSS_SELECTOR, Locator.dropdown_selection+f':nth-of-type(2)').text).replace('\n×', '')

    browser.find_element(By.CSS_SELECTOR, Locator.dropdown_handle).click()
    browser.find_element(By.CSS_SELECTOR, Locator.clear_btn).click()
    assert browser.find_element(By.CSS_SELECTOR, Locator.dropdown_placeholder_text).get_attribute('placeholder') == 'Select peoples'
    browser.quit()