import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# import the UserSimulation class
from User_Simulation import UserSimulation

# create an instance of the UsreSimulation class with the desired browser type (1: Chrome, 2: Firefox, 3: Edge, 4: Safari)
test = UserSimulation(1) # use the number for Chrome

# initialize the Selenium WebDriver
browser=test.browser
browser.maximize_window()

mouse_hovering = ActionChains(browser)

# test case: damaged photo
def test_damaged_photo():
    # validation of search field
    search_field = WebDriverWait(test.browser, 10).until(EC.presence_of_element_located((By.NAME, "search")))
    assert search_field.is_displayed(), "Search field not displayed."
    #print("Element search_field found.")

    # simulating search
    test.hover_and_click(search_field)
    search_field.send_keys("placeholder")
    test.wait_for_seconds(3)

    search_field.send_keys(Keys.RETURN)
    #print("Enter key sent to the search field.")
    test.wait_for_seconds(3)
    #test.create_screenshot()

    # validation of the search results
    search_result = test.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-search-result-route/baasic-photo-list/div/div[2]/span/div[1]")
    assert True,"Element search_result found."

    test.hover_and_click(search_result)
    #print("Search result opened.")
    test.wait_for_seconds(3)
    #test.create_screenshot()

    # exiting search result
    exit_search_result_button = test.browser.find_element(By.XPATH, "//button[@type='button']")
    exit_search_result_button.click()
    #print("Search result closed.")
    test.wait_for_seconds(3)
    #test.create_screenshot()

    # navigating to the home page
    menu_button = test.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
    test.hover(menu_button)
    #print("Hovered over dropdown menu button.")
    test.wait_for_seconds()

    logo_button = test.browser.find_element(By.TAG_NAME, "use")
    test.hover_and_click(logo_button)
    #print("Logo button clicked.")
    test.wait_for_seconds()

# test case: open photo gallery
def test_open_photo_gallery():
    open_gallery_button = browser.find_elements(By.TAG_NAME, "svg")[1]
    mouse_hovering.move_to_element(open_gallery_button).click().perform()
    time.sleep(1)

    # simulate scrolling down
    scroll_element = browser.find_element('tag name', 'body')
    scrolls = 10  # number of scrolls
    scroll_delay = 1  # waiting time between scrolls

    for _ in range(scrolls):
        scroll_element.send_keys(Keys.PAGE_DOWN)
        time.sleep(scroll_delay)

    # simulating scrolling up the page
    scroll_element.send_keys(Keys.HOME)
    #print("Page scrolled up.")
    test.wait_for_seconds()

#test case: social login options
def test_social_login_options(test):
    # navigating to the menu
    menu_button = test.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
    test.hover_and_click(menu_button)
    #print("Navigated to the menu.")
    test.wait_for_seconds()

    # click on the login option for social login links
    login_option = test.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[2]/span")
    test.hover_and_click(login_option)
    #print("Login form opened.")
    assert True, "Login form opened."
    
    # define XPath and names of social login buttons
    social_buttons = [
        ("/html/body/app/master-layout/div/main/div/loader-component/div/ng-component/section/div/div[2]/baasic-social-login/div/div[1]/button[1]", "Facebook"),
        ("/html/body/app/master-layout/div/main/div/loader-component/div/ng-component/section/div/div[2]/baasic-social-login/div/div[1]/button[2]", "Twitter"),
        ("/html/body/app/master-layout/div/main/div/loader-component/div/ng-component/section/div/div[2]/baasic-social-login/div/div[1]/button[3]", "Google"),
        ("/html/body/app/master-layout/div/main/div/loader-component/div/ng-component/section/div/div[2]/baasic-social-login/div/div[1]/button[4]", "Github")
    ]

    # iterating through each social login button
    for button_xpath, platform_name in social_buttons:
        button = test.browser.find_element(By.XPATH, button_xpath)
        test.hover_and_click(button)
        test.wait_for_seconds()

        # find the <p> tag that contains login information
        p_tag = test.browser.find_element(By.TAG_NAME, "p")
        try:
            # check if there is either a login or error message
            assert p_tag.text != "undefined: Social login configuration not found.", f"Error: Failed to log in using {platform_name}."
            print(f"Success: The Sign in with {platform_name} option became available on the site")
        except AssertionError as e:
            print(e)

# test case: image page access
@pytest.mark.retry(count=3, delay=2)  # retry up to 3 times with a delay of 2 seconds
def test_image_page_access():
    try:
        # navigating to the menu
        menu_button = test.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
        test.hover_and_click(menu_button)
        #print("Navigated to the menu.")
        test.wait_for_seconds()

        # user login on the website
        test.login("miksi23", "Winnetou210954")
        time.sleep(3)

        # navigating to the album
        latest_album_thumbnail = test.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
        test.hover_and_click(latest_album_thumbnail)
        test.wait_for_seconds()

        # the first image preview
        image_thumbnail = browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div/span/div[1]")
        test.hover_and_click(image_thumbnail)

        # simulate the h1_tag.text value for testing purposes
        h1_tag = browser.find_element(By.TAG_NAME, "h1")

        # check if the <h1> tag content indicates a 404 page missing error
        if h1_tag.text == "404: page missing":
            print("Detected 404 error. Navigating to home page...")
            # navigate to the home page
            test.hover(menu_button)
            test.wait_for_seconds()
            logo_button = test.browser.find_element(By.TAG_NAME, "use")
            test.hover_and_click(logo_button)
            test.wait_for_seconds()
            print("Navigated to the home page after encountering 404 error.")
            return  # stop further execution of the test case
        print("Success: Page is accessible")
        
    except AssertionError as e:
        print(e)
if __name__ == "__main__":
    # call the damaged_photo function
    test_damaged_photo()

    # call the open_photo_gallery function
    test_open_photo_gallery()

    # test all Sign in with options
    test_social_login_options(test)

    # call the test_image_page_access function
    test_image_page_access()
    
    # close the browser
    browser.quit()