import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# list of usernames and passwords to test
credentials = [
   ("miksi", "Winnetou018"),
    ("MIKSI", "Winnetou018"),
    ("miksi", "winnetou018"),
    ("", ""), 
    ("", "Winnetou018"),
    ("miksi", " "),
    ("mkiis", "Winnetou018"),
    ("miksi", "Winetou018"),
    ("user123", "Passw0rd!"), 
    ("miksi", "InvalidPassword"),  
    ("invalidusername", "Winnetou018"),  
    ("nonexistentuser", "InvalidPassword")
]

def wait_for_seconds(seconds=1):
    time.sleep(seconds)

# wait for an element to appear on the page.
def wait_for_element(browser, by, value, timeout=10):
    wait = WebDriverWait(browser, timeout) # maximum waiting time in seconds: default is 10
    return wait.until(EC.presence_of_element_located((by, value))) # returns: the found web element

def test_login(browser, username, password):
    # call the login function with the username and password
    username_field = browser.find_element(By.NAME, "username")
    username_field.send_keys(username)
    wait_for_seconds()

    password_field = browser.find_element(By.NAME, "password")
    password_field.send_keys(password)
    browser.implicitly_wait(3)
    wait_for_seconds()

    # click on the login button to submit the credentials
    login_button = browser.find_elements(By.TAG_NAME, "button")[0]
    login_button.click()
    browser.implicitly_wait(1)

if __name__ == "__main__":
    website_url = "http://demo.baasic.com/angular/starterkit-photo-gallery/login"

    for username, password in credentials:
        browser = Chrome()
        browser.maximize_window()
        browser.get(website_url)
        test_login(browser, username, password)
       
        # check if the "Create Album" button is present
        create_album_button_present = False  # assume the button is not present
        try:
            create_album_button = browser.find_element(By.XPATH, "//button[text()='Create Album']")
            create_album_button_present = True
        except NoSuchElementException:
            pass  # the button is not present

        result = "SUCCESS" if create_album_button_present else "FAILURE"
        print(f"Login {result} for username: '{username}' and password: '{password}'")

            
        time.sleep(1)  # pause between test cases
        browser.quit()  # close the browser after each test case
