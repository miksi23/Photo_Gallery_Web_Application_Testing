# test_user_simulation.py
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from User_Simulation import UserSimulation

browser= webdriver.Chrome()
browser.maximize_window()

mouse_hovering = ActionChains(browser)

test = UserSimulation(1)

def test_run_test():
    test = UserSimulation(1) # use the number for Chrome
    test.run_test()

def damaged_photo():
    # validation of search field
    search_field = WebDriverWait(test.browser, 10).until(EC.presence_of_element_located((By.NAME, "search")))
    assert search_field.is_displayed(), "Search field not displayed."
    print("Element search_field found.")

    # simulating search
    test.hover_and_click(search_field)
    search_field.send_keys("placeholder")
    test.wait_for_seconds(3)

    search_field.send_keys(Keys.RETURN)
    print("Enter key sent to the search field.")
    test.wait_for_seconds(3)
    #test.create_screenshot()

    # validation of the search results
    search_result = test.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-search-result-route/baasic-photo-list/div/div[2]/span/div[1]")
    assert True,"Element search_result found."

    test.hover_and_click(search_result)
    print("Search result opened.")
    test.wait_for_seconds(3)
    #test.create_screenshot()

    # exiting search result
    exit_search_result_button = test.browser.find_element(By.XPATH, "//button[@type='button']")
    exit_search_result_button.click()
    print("Search result closed.")
    test.wait_for_seconds(3)
    #test.create_screenshot()

    # navigating to the home page
    menu_button = test.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
    test.hover(menu_button)
    print("Hovered over dropdown menu button.")
    test.wait_for_seconds()

    logo_button = test.browser.find_element(By.TAG_NAME, "use")
    test.hover_and_click(logo_button)
    print("Logo button clicked.")
    test.wait_for_seconds()

def open_photo_gallery():
    open_gallery_button = browser.find_elements(By.TAG_NAME, "svg")[1]
    mouse_hovering.move_to_element(open_gallery_button).click().perform()
    time.sleep(1)

    # simulate scrolling down
    scroll_element = browser.find_element('tag name', 'body')
    scrolls = 10  # number of scrolls
    scroll_delay = 2  # waiting time between scrolls

    for _ in range(scrolls):
        scroll_element.send_keys(Keys.PAGE_DOWN)
        time.sleep(scroll_delay)


    # simulating scrolling up the page
    scroll_element.send_keys(Keys.HOME)
    print("Page scrolled up.")
    test.wait_for_seconds()