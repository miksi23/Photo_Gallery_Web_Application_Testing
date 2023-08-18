import os
import time
from datetime import datetime

from selenium.webdriver import Chrome, Edge, Firefox, Safari
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# import the AlbumPage class
from Album_Page import AlbumPage


class UserSimulation:
    def __init__(self, browser_type):
        # defining paths to files that will be used for testing
        self.screenshot_path = os.path.abspath(r"C:\Users\User\Desktop\radna verzija\screenshot.png")
        self.cover_photo_path = os.path.abspath(r"C:\Users\User\Desktop\radna verzija\cat-ga2192b34a_128012345111.jpg")
        self.new_cover_photo_path = os.path.abspath(r"C:\Users\User\Desktop\radna verzija\seashells-g10fcd89cc_12801234523456.jpg")
        self.image1_path = os.path.abspath(r"C:\Users\User\Desktop\radna verzija\igu-dfhadgg63ec0bd99_1280.jpg")
        self.image2_path = os.path.abspath(r"C:\Users\User\Desktop\radna verzija\marguerite-gc981fd054_1280112.jpg")

        self.browser_type = browser_type
        self.browser = self.get_browser()
        self.browser.maximize_window()
        self.browser.get('http://demo.baasic.com/angular/starterkit-photo-gallery/main')

        self.mouse_hovering = ActionChains(self.browser)
        self.wait = WebDriverWait(self.browser, 10)

    def get_browser(self):
        # mapping numbers to corresponding web browsers
        valid_browser = False  # initialize valid_browser to False
        browser_mapping = {
            1: Chrome,
            2: Firefox,
            3: Edge,
            4: Safari
        }

        try:
            browser = browser_mapping[self.browser_type]()
            valid_browser = True
        except KeyError:
            print("Invalid browser number. Enter 1, 2, 3, or 4.")
            return None

        return browser

    @staticmethod
    def wait_for_seconds(seconds=1):
        """
        a helper function that creates a pause in code execution for a specified number of seconds
    
        arguments:
        seconds (int or float, optional): the time of the pause in seconds, default number of seconds to wait is 1 second
        """
        time.sleep(seconds)

    def hover_and_click(self, element):
        # simulates hover and click on element
        self.mouse_hovering.move_to_element(element).click().perform()
        self.wait_for_seconds()

    def hover(self, element):
        # simulates hover on element
        self.mouse_hovering.move_to_element(element).perform()

    def create_screenshot(self):
        # creates a screenshot of the web browser
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        screenshot_name = f"screenshot_{timestamp}.png"
        self.browser.save_screenshot(screenshot_name)
        print(f"Screenshot created: {screenshot_name}")

    def login(self, username, password):
        # click on the login option to open the login form
        login_option = self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[2]/span")
        self.hover_and_click(login_option)
        print("Login form opened.")
        assert True, "Login form opened."

        # simulates user login on the website
        # enter the username and password into the respective fields
        username_field = self.browser.find_element(By.NAME, "username")
        username_field.send_keys(username)
        self.wait_for_seconds()

        password_field = self.browser.find_element(By.NAME, "password")
        password_field.send_keys(password)
        print("Entered username and password.")
        self.browser.implicitly_wait(3)
        self.wait_for_seconds()

        # click on the login button to submit the credentials
        login_button = self.browser.find_elements(By.TAG_NAME, "button")[0]
        login_button.click()
        print("Login successful!")
        self.browser.implicitly_wait(3)

    def run_test(self):      
        # runs the website functionality test
        try:
            # validation of search field
            search_field = self.wait.until(EC.presence_of_element_located((By.NAME, "search")))
            assert search_field.is_displayed(), "Search field not displayed."
            print("Element search_field found.")

            # simulating search
            self.hover_and_click(search_field)
            search_field.send_keys("pas")
            self.wait_for_seconds()

            search_field.send_keys(Keys.RETURN)
            print("Enter key sent to the search field.")
            self.wait_for_seconds()

            # simulating scrolling down the page
            scroll_element = self.browser.find_element('tag name', 'body')
            scroll_element.send_keys(Keys.PAGE_DOWN)
            print("Page scrolled down.")
            self.wait_for_seconds()

            # simulating scrolling up the page
            scroll_element.send_keys(Keys.HOME)
            print("Page scrolled up.")
            self.wait_for_seconds()

            # validation of the search results
            search_result = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-search-result-route/baasic-photo-list/div/div[2]/span/div[1]")))
            assert True,"Element search_result found."

            self.hover_and_click(search_result)
            print("Search result opened.")
            self.wait_for_seconds()

            # exiting search result
            exit_search_result_button = self.browser.find_element(By.XPATH, "//button[@type='button']")
            exit_search_result_button.click()
            print("Search result closed.")
            self.wait_for_seconds()

            # validation of dropdown menu button
            menu_button = self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
            self.hover_and_click(menu_button)
            print("Clicked on the dropdown menu button.")

            # validation of dropdown home button
            self.hover(menu_button)
            print("Hovered over dropdown menu button.")
            self.wait_for_seconds()

            logo_button = self.browser.find_element(By.TAG_NAME, "use")
            self.hover_and_click(logo_button)
            print("Logo button clicked.")
            self.wait_for_seconds()

            # navigating to the menu
            self.hover_and_click(menu_button)
            print("Navigated to the menu.")
            self.wait_for_seconds()

            # login form validation
            self.login("miksi23", "Winnetou210954")
            print("Login button clicked.")

            # album creation
            self.create_album_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div/div[2]/button")
            self.create_album_button.click()
            print("Create album button clicked.")
            self.wait_for_seconds()

            album_name_element=self.browser.find_element(By.ID,"albumName")
            album_name_element.send_keys("my first album")
            self.wait_for_seconds()

            album_description_element=self.browser.find_element(By.ID,"albumDescription")
            album_description_element.send_keys("describing my first album, but actually, I want to test the BACK button...")
            self.wait_for_seconds()

            # back button validation
            back_button=self.browser.find_elements(By.TAG_NAME,"button")[0]
            back_button.click()
            print("Back button clicked.")
            self.wait_for_seconds()

            # create an instance of the AlbumPage class and pass the browser to it
            Album_Page = AlbumPage(test.browser)

            # new album creation
            # calling methods on the AlbumPage object
            Album_Page.create_album("my first album, second attempt", "describing my first album, second attempt")
            print("Save album button click validated.")
            self.wait_for_seconds()

            # cover photo upload
            upload_cover_photo_field=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-album-create-route/div/div/div/div[1]")
            upload_cover_photo_field.click()
            self.wait_for_seconds()

            Album_Page.upload_photo(self.cover_photo_path, "describing the cover photo")

            # album creation validation
            print("Album created.")

            # back to album
            latest_album_thumbnail=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
            self.hover_and_click(latest_album_thumbnail)
            self.wait_for_seconds()

            # upload photo
            upload_photo_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[3]/button")
            upload_photo_button.click()
            self.wait_for_seconds()

            Album_Page.upload_photo(self.image1_path, "describing my first photo")

            # returning to albums
            go_back_to_albums_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[1]/button")
            go_back_to_albums_button.click()
            print("Validation of the go back to albums button click successful.")
            self.wait_for_seconds()

            # back to album
            latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]")
            self.hover_and_click(latest_album_thumbnail)
            print("Latest album thumbnail clicked.")

            # second image upload
            upload_photo_brown_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[3]")
            upload_photo_brown_button.click()
            self.wait_for_seconds()

            Album_Page.upload_photo(self.image2_path, "describing the second image")

            # returning to albums
            go_back_to_albums_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[1]/button")
            go_back_to_albums_button.click()
            self.wait_for_seconds()

            # back to album
            latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]")
            self.hover_and_click(latest_album_thumbnail)
            print("Latest album thumbnail clicked.")

            # second uploaded image preview
            second_image_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div[2]/span/div[1]")
            self.hover_and_click(second_image_thumbnail)
            print("Second image thumbnail clicked.")

            # forward arrow
            second_image_arrow_right=second_image_arrow_left= self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-of-type(3)")))
            second_image_arrow_right.click()
            print("Forward arrow clicked.")
            self.wait_for_seconds()

            # backward arrow
            second_image_arrow_left= self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-of-type(2)")))
            second_image_arrow_left.click()
            print("Backward arrow clicked.")
            self.wait_for_seconds()

            # close button verification
            close_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn--med.btn--ghost.pos--custom.type--negative[title='Close photo']")))
            close_button.click()
            print("Close image button click validated.")
            self.wait_for_seconds()

            # second image deleting
            second_image_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div[2]/span/div[1]")
            self.hover(second_image_thumbnail)
            self.wait_for_seconds()

            delete_second_image_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div[2]/span/div[1]/div[3]/div/button")
            self.hover_and_click(delete_second_image_button)
            self.wait_for_seconds()

            Album_Page.delete_photo()

            # returning to albums
            go_back_to_albums_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[1]/button")
            go_back_to_albums_button.click()
            self.wait_for_seconds()

            # back to album
            latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]")
            self.hover_and_click(latest_album_thumbnail)

            # image deleting
            image_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div/span/div[1]")
            self.hover(image_thumbnail)
            self.wait_for_seconds()

            delete_image_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div[1]/span/div[1]/div[3]/div/button")
            self.hover_and_click(delete_image_button)

            # checking cancel delete photo button functionality
            cancel_image_delete=self.browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--primary']")
            cancel_image_delete.click()
            print("Validation of the cancel image delete button click successful.")

            # latest photo deleting
            image_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div/span/div[1]")
            self.hover(image_thumbnail)
            self.wait_for_seconds()

            delete_image_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div[1]/span/div[1]/div[3]/div/button")
            self.hover_and_click(delete_image_button)

            Album_Page.delete_photo()

            print("Successfully deleted the latest photo.")
            self.wait_for_seconds()

            # returning to albums
            go_back_to_albums_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[1]/button")
            go_back_to_albums_button.click()
            self.wait_for_seconds()

            # changing cover photo
            latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
            self.hover(latest_album_thumbnail)
            self.wait_for_seconds()

            upload_cover_photo_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]/div[3]/button")
            upload_cover_photo_button.click()
            self.wait_for_seconds()

            Album_Page.upload_photo(self.new_cover_photo_path, "describing the new cover photo")

            # album delete
            latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]") # refreshing the reference to latest_album_thumbnail
            self.hover(latest_album_thumbnail)
            self.wait_for_seconds()

            delete_album_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]/div[4]/button")
            delete_album_button.click()
            self.wait_for_seconds()
          
            # checking cancel delete album button functionality
            cancel_album_delete=self.browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--primary']")
            cancel_album_delete.click()
            print("Cancel delete album button click validated.")

            # latest album delete
            latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
            self.hover(latest_album_thumbnail)
            self.wait_for_seconds()

            delete_album_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]/div[4]/button")
            delete_album_button.click()
            self.wait_for_seconds()

            Album_Page.delete_album()

            # navigating to the menu
            menu_button = self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
            self.hover_and_click(menu_button)
            self.wait_for_seconds()

            # profile option verification
            profile_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[1]/span")
            self.hover(profile_button)

            print("Profile button hovered.")

            # testing mouse hover reaction
            #self.create_screenshot()
            self.wait_for_seconds()

            profile_button.click()

            print("Profile page opened.")
            self.wait_for_seconds()

            # navigating to the menu
            self.hover_and_click(menu_button)
            self.wait_for_seconds()

            # create album option verification
            create_album_option=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[2]/span")
            self.hover(create_album_option)

            print("Create album option hovered.")

            # testing mouse hover reaction
            #self.create_screenshot()
            self.wait_for_seconds()

            create_album_option.click()

            print("Create album page opened.")
            self.wait_for_seconds()

            # navigating to the menu
            self.hover_and_click(menu_button)
            self.wait_for_seconds()

            # logout option verification
            logout_option=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/baasic-logout/li/span")
            self.hover(logout_option)

            print("Logout option hovered.")

            # testing mouse hover reaction
            #self.create_screenshot()
            self.wait_for_seconds()

            logout_option.click()
            print("Logged out.")
            self.wait_for_seconds()

            # take a screenshot after the testing is finished
            #self.create_screenshot()

        except Exception as e:
            # if an exception occurs, we handle the error here
            print(f"An error occurred while executing the test: {e}")

        finally:
            # finally, always close the browser, regardless of whether an error occurred or not
            self.browser.quit()

if __name__ == "__main__":
    # code that runs when the file is executed directly
    test = UserSimulation(1) # use browser type number (1: Chrome, 2: Firefox, 3: Edge, 4: Safari)

    if test.browser is None:
        print("Failed to get the browser. Check the validity of the browser number (1: Chrome, 2: Firefox, 3: Edge, 4: Safari).")
    else:
        # test execution
        test.run_test()
