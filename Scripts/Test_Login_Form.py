import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# list of usernames and passwords to test
credentials = [
    ("miksi", "Winnetou018"),
    ("MIKSI", "Winnetou018"),
    ("miksi", "winnetou018"),
    ("", ""),
    ("", "Winnetou018"),
    ("miksi", " "),
    ("mkiis", "Winnetou018"),
    ("miksi", "Winetou18"),
    ("user123", "Passw0rd!"), 
    ("miksi", "InvalidPassword"),  
    ("invalidusername", "Winnetou018"),  
    ("nonexistentuser", "InvalidPassword")
]

# fixture to manage browser instance
@pytest.fixture
def browser():
    browser = Chrome()  # create a new Chrome browser instance
    browser.maximize_window()  # maximize the browser window for better visibility
    yield browser  # yield the browser instance to the test
    browser.quit()  # quit the browser and release resources after the test

# test for successful login
@pytest.mark.parametrize("username, password", credentials)
def test_successful_login(browser, username, password):
    browser.get("http://demo.baasic.com/angular/starterkit-photo-gallery/login")  # open the login page
    # call the login function with the provided username and password
    username_field = browser.find_element(By.NAME, "username")
    username_field.send_keys(username)
    password_field = browser.find_element(By.NAME, "password")
    password_field.send_keys(password)
    login_button = browser.find_elements(By.TAG_NAME, "button")[0]
    login_button.click()

    try:
        create_album_button = browser.find_element(By.XPATH, "//button[text()='Create Album']")
        assert True  # if the button is found, assert success
    except NoSuchElementException:
        assert False  # if the button is not found, assert failure

# test for unsuccessful login
@pytest.mark.parametrize("username, password", credentials)
def test_unsuccessful_login(browser, username, password):
    browser.get("http://demo.baasic.com/angular/starterkit-photo-gallery/login")  # open the login page
    # call the login function with the provided username and password
    username_field = browser.find_element(By.NAME, "username")
    username_field.send_keys(username)
    password_field = browser.find_element(By.NAME, "password")
    password_field.send_keys(password)
    login_button = browser.find_elements(By.TAG_NAME, "button")[0]
    login_button.click()

    try:
        create_album_button = browser.find_element(By.XPATH, "//button[text()='Create Album']")
        assert False  # if the button is found, assert failure
    except NoSuchElementException:
        assert True  # if the button is not found, assert success

