import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome, Edge, Firefox, Safari
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = Chrome()
browser.maximize_window()
browser.get('http://demo.baasic.com/angular/starterkit-photo-gallery/main')

mouse_hovering = ActionChains(browser)
wait = WebDriverWait(browser, 10)

# list of image XPaths to test
base_image_xpath = "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div"
image_indices = list(range(1, 12))
image_xpaths = [f"{base_image_xpath}[{index}]" for index in image_indices]

# helper functions
def wait_for_seconds(seconds=1):
    time.sleep(seconds)

def hover(element):
    # simulates hover on element
    mouse_hovering.move_to_element(element).perform()

def hover_and_click(element):
    # simulates hover and click on element
    mouse_hovering.move_to_element(element).click().perform()
    wait_for_seconds()

# find element with retry
def find_element_with_retry(by, value, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            element = browser.find_element(by, value)
            return element
        except NoSuchElementException:
            retries += 1
            print(f"Element not found. Retrying... Attempt {retries}/{max_retries}")
            time.sleep(2)  # wait before retrying
    return None

# log in to the website
def perform_login():
    # navigate to the menu
    menu_button = browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
    hover_and_click(menu_button)
    wait_for_seconds()

    # click on the login option to open the login form
    login_option = browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[2]/span")
    hover_and_click(login_option)

    # user login on the website
    username_field = browser.find_element(By.NAME, "username")
    username_field.send_keys("miksi23")
    wait_for_seconds()

    password_field = browser.find_element(By.NAME, "password")
    password_field.send_keys("Winnetou210954")
    browser.implicitly_wait(3)
    wait_for_seconds()

    # click on the login button to submit the credentials
    login_button = browser.find_elements(By.TAG_NAME, "button")[0]
    login_button.click()
    browser.implicitly_wait(3)

    # navigating to the album
    latest_album_thumbnail = browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
    latest_album_thumbnail.click()
    time.sleep(2)

# test image page access
@pytest.mark.retry(count=3, delay=2)  # retry up to 3 times with a delay of 2 seconds
def test_image_page_access(image_xpaths):
    try:
        # iterate through the list of image XPaths and click each image
        for image_index, image_xpath in enumerate (image_xpaths, start=1):
            # re-find the image element before interacting with it
            image_thumbnail = find_element_with_retry(By.XPATH, image_xpath)
            if image_thumbnail:
                # scroll down to make the image visible before clicking
                browser.execute_script("arguments[0].scrollIntoView();", image_thumbnail)
                image_thumbnail.click()
                time.sleep(2)

            # check if the <h1> tag content indicates a 404 page missing error
            try:
                h1_tag = browser.find_element(By.TAG_NAME, "h1")

                # if h1 tag with "404: page missing" text exists, image encountered an error
                if h1_tag.text == "404: page missing":
                    print(f"Image at position {image_index}: encountered a 404 error and could not be opened.")
                    
                    # navigate to the album page
                    menu_button = browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
                    hover_and_click(menu_button)
                    wait_for_seconds()
                    profile_button = browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[1]/span")
                    hover(profile_button)
                    wait_for_seconds()
                    profile_button.click()
                    latest_album_thumbnail = browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
                    hover_and_click(latest_album_thumbnail)
                    wait_for_seconds()
            except NoSuchElementException:
                    print(f"Image at position {image_index}: can be opened successfully.")

                    # navigate to the album page
                    close_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn--med.btn--ghost.pos--custom.type--negative[title='Close photo']")))
                    close_button.click()
                    wait_for_seconds()

    except Exception as e:
         print(f"An error occurred with image at position {image_index}: {e}")

    finally:
        # close the browser
        browser.quit()

perform_login()

# run the test case with the list of image XPaths
test_image_page_access(image_xpaths)