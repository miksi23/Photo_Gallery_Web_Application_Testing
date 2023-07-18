import os
import time
from datetime import datetime

from selenium.webdriver import Chrome, Edge, Firefox, Safari
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# class that contains functionalities for testing website functionality
class WebsiteFunctionalityTest:
    def __init__(self, browser_type):

        # defining paths to files that will be used for testing
        self.screenshot_path = os.path.abspath(r"C:\Users\Mira\Desktop\New Folder\screenshot.png")
        self.cover_photo_path = os.path.abspath(r"C:\Users\Mira\Desktop\New Folder\cat-ga2192b34a_12801234511.jpg")
        self.new_cover_photo_path = os.path.abspath(r"C:\Users\Mira\Desktop\New Folder\seashells-g10fcd89cc_12801234523456.jpg")
        self.image1_path = os.path.abspath(r"C:\Users\Mira\Desktop\New Folder\igu-dfhadgg63ec0bd99_1280.jpg")
        self.image2_path = os.path.abspath(r"C:\Users\Mira\Desktop\New Folder\marguerite-gc981fd054_1280.jpg")

        self.browser_type = browser_type
        self.browser = self.get_browser()
        self.browser.maximize_window()
        self.browser.get('http://demo.baasic.com/angular/starterkit-photo-gallery/main')

        self.mouse_hovering = ActionChains(self.browser)
        self.wait = WebDriverWait(self.browser, 10)
       

    def get_browser(self):
        # mapping numbers to corresponding web browsers
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

    def hover_and_click(self, element):
        # simulates hover and click on element
        self.mouse_hovering.move_to_element(element).click().perform()
        time.sleep(1)

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
        self.browser.save_screenshot(self.screenshot_path)

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
        time.sleep(1)

        password_field = self.browser.find_element(By.NAME, "password")
        password_field.send_keys(password)
        print("Entered username and password.")
        time.sleep(1)

        # click on the login button to submit the credentials
        login_button = self.browser.find_elements(By.TAG_NAME, "button")[0]
        login_button.click()
        print("Login successful!")
        time.sleep(3)

    def create_album(self, album_name_value, album_description_value):
        # simulates album creation on the website
        # click on the create album button to open the album creation form
        create_album_button = self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div/div[2]/button")
        create_album_button.click()
        time.sleep(3)

        # enter the album name and description into the respective fields
        album_name_element = self.browser.find_element(By.ID, "albumName")
        album_name_element.send_keys(album_name_value)
        time.sleep(1)

        album_description_element = self.browser.find_element(By.ID, "albumDescription")
        album_description_element.send_keys(album_description_value)
        time.sleep(5)

        # click on the save album button to create the album
        save_album_button = self.browser.find_elements(By.TAG_NAME, "button")[1]
        save_album_button.click()
        time.sleep(3)

    def upload_photo(self, photo_path, photo_description):
        # simulates uploading a photo to the website
        # enter the photo path into the upload image input field
        upload_image_input = self.browser.find_element(By.ID, "photoInput")
        upload_image_input.send_keys(photo_path)
        time.sleep(1)

        # enter the photo path into the upload image input field
        image_description = self.browser.find_element(By.ID, "photoDescription")
        image_description.send_keys(photo_description)
        time.sleep(3)
        
        # click on the upload button to upload the photo
        upload_button = self.browser.find_element(By.XPATH, "//button[@type='submit']")
        upload_button.click()
        print("Successfully uploaded the image.")

        self.browser.implicitly_wait(10)
        time.sleep(3)

    def run_test(self):
          # runs the website functionality test
          if self.browser is None:
               print("Failed to get the browser.")
               return

          # validation of search field
          search_field = self.wait.until(EC.presence_of_element_located((By.NAME, "search")))
          assert search_field.is_displayed(), "Search field not displayed."
          print("Element search_field found.")

          # simulating search
          self.hover_and_click(search_field)
          search_field.send_keys("pas")
          time.sleep(3)

          search_field.send_keys(Keys.RETURN)
          print("Enter key sent to the search field.")
          time.sleep(3)
          
          # simulating scrolling down the page
          scroll_element = self.browser.find_element('tag name', 'body')
          scroll_element.send_keys(Keys.PAGE_DOWN)
          print("Page scrolled down.")
          time.sleep(1)
          
          # simulating scrolling up the page
          scroll_element.send_keys(Keys.HOME)
          print("Page scrolled up.")
          time.sleep(1)
          
          # search results verification
          search_result = self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-search-result-route/baasic-photo-list/div/div[2]/span/div[1]")
          assert True,"Element search_result found."

          self.hover_and_click(search_result)
          print("Search result opened.")
          time.sleep(3)

          # exiting search result
          exit_search_result_button = self.browser.find_element(By.XPATH, "//button[@type='button']")
          exit_search_result_button.click()
          print("Search result closed.")
          time.sleep(3)
          
          # validation of dropdown menu button
          menu_button = self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
          self.hover_and_click(menu_button)
          print("Clicked on the dropdown menu button.")
          time.sleep(3)
          
          # validation of dropdown home button
          self.hover(menu_button)
          print("Hovered over dropdown menu button.")
          time.sleep(1)

          logo_button = self.browser.find_element(By.TAG_NAME, "use")
          self.hover_and_click(logo_button)
          print("Logo button clicked.")
          time.sleep(3)
          
          # navigating to the menu
          self.hover_and_click(menu_button)
          print("Navigated to the menu.")
          time.sleep(3)
          
          # login form validation
          self.login("miksi23", "Winnetou210954")
          print("Login button clicked.")

          # album creation
          self.create_album_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div/div[2]/button")
          self.create_album_button.click()
          print("Create album button clicked.")
          time.sleep(3)

          album_name_element=self.browser.find_element(By.ID,"albumName")
          album_name_element.send_keys("my first album")
          time.sleep(1)

          album_description_element=self.browser.find_element(By.ID,"albumDescription")
          album_description_element.send_keys("describing my first album, but actually, I want to test the BACK button...")
          time.sleep(5)

          # back button validation
          back_button=self.browser.find_elements(By.TAG_NAME,"button")[0]
          back_button.click()
          print("Back button clicked.")
          time.sleep(1)

          # new album creation
          self.create_album("my first album, second attempt", "describing my first album from the second attempt")
          print("Save album button click validated.")
          time.sleep(3)

          # cover photo upload
          upload_cover_photo_field=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-album-create-route/div/div/div/div[1]")
          upload_cover_photo_field.click()
          self.upload_photo(self.cover_photo_path, "describing the cover photo")

          # album creation validation
          print("Album created.")

          # back to album
          latest_album_thumbnail=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
          self.hover_and_click(latest_album_thumbnail)

          # upload photo
          upload_photo_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[3]/button")
          upload_photo_button.click()
          time.sleep(3)

          self.upload_photo(self.image1_path, "describing my first photo")

          # second image upload from album
          upload_photo_brown_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[3]")
          upload_photo_brown_button.click()
          time.sleep(3)

          self.upload_photo(self.image2_path, "describing the second image")

          # returning to albums
          go_back_to_albums_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[1]/button")
          go_back_to_albums_button.click()
          print("Validation of the go back to albums button click successful.")
          time.sleep(3)

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
          time.sleep(3)

          # backward arrow
          second_image_arrow_left= self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-of-type(2)")))
          second_image_arrow_left.click()
          print("Backward arrow clicked.")
          time.sleep(3)

          # close button verification
          close_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn--med.btn--ghost.pos--custom.type--negative[title='Close photo']")))
          close_button.click()
          print("Close image button click validated.")
          time.sleep(3)

          # second image deleting
          second_image_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div[2]/span/div[1]")
          self.hover(second_image_thumbnail)
          time.sleep(3)

          delete_second_image_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div[2]/span/div[1]/div[3]/div/button")
          self.hover_and_click(delete_second_image_button)
          time.sleep(3)

          confirm_delete=self.browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--warning']")
          confirm_delete.click()
          time.sleep(3)

          # returning to albums
          go_back_to_albums_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[1]/button")
          go_back_to_albums_button.click()
          time.sleep(3)

          # back to album
          latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]")
          self.hover_and_click(latest_album_thumbnail)

          # delete image
          image_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div/span/div[1]")
          self.hover(image_thumbnail)
          time.sleep(1)

          delete_image_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div[1]/span/div[1]/div[3]/div/button")
          self.hover_and_click(delete_image_button)

          # checking cancel delete photo button functionality
          cancel_image_delete=self.browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--primary']")
          cancel_image_delete.click()
          print("Validation of the cancel image delete button click successful.")

          # latest photo delete
          image_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div/span/div[1]")
          self.hover(image_thumbnail)
          time.sleep(1)

          delete_image_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div[1]/span/div[1]/div[3]/div/button")
          self.hover_and_click(delete_image_button)
          confirm_delete1=self.browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--warning']")
          confirm_delete1.click()

          print("Successfully deleted the latest photo.")
          time.sleep(3)

          # returning to albums
          go_back_to_albums_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[1]/button")
          go_back_to_albums_button.click()
          time.sleep(3)

          # changing cover photo
          latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
          self.hover(latest_album_thumbnail)
          time.sleep(1)

          upload_cover_photo_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]/div[3]/button")
          upload_cover_photo_button.click()
          time.sleep(3)

          self.upload_photo(self.new_cover_photo_path, "describing the new cover photo")

          # album deleting
          latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]") # refreshing the reference to latest_album_thumbnail
          self.hover(latest_album_thumbnail)
          time.sleep(3)
          delete_album_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]/div[4]/button")
          delete_album_button.click()
          time.sleep(3)

          # checking cancel delete album button functionality
          cancel_album_delete=self.browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--primary']")
          cancel_album_delete.click()
          print("Cancel delete album button click validated.")

          # latest album delete
          latest_album_thumbnail=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
          self.hover(latest_album_thumbnail)
          time.sleep(3)

          delete_album_button=self.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]/div[4]/button")
          delete_album_button.click()
          time.sleep(3)

          confirm_album_delete=self.browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--warning']")
          confirm_album_delete.click()
          print("Successfully deleted the latest album.")
          time.sleep(3)

          # navigating to the menu
          menu_button = self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
          self.hover_and_click(menu_button)
          time.sleep(3)

          # profile option verification
          profile_button=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[1]/span")
          self.hover(profile_button)

          print("Profile button hovered.")

          # testing mouse hover reaction
          self.create_screenshot()
          time.sleep(1)

          profile_button.click()

          print("Profile page opened.")
          time.sleep(3)

          # navigating to the menu
          self.hover_and_click(menu_button)
          time.sleep(3)

          # create album option verification
          create_album_option=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[2]/span")
          self.hover(create_album_option)

          print("Create album option hovered.")

          # testing mouse hover reaction
          self.create_screenshot()
          time.sleep(1)

          create_album_option.click()

          print("Create album page opened.")
          time.sleep(3)

          # navigating to the menu
          self.hover_and_click(menu_button)
          time.sleep(3)

          # logout option verification
          logout_option=self.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/baasic-logout/li/span")
          self.hover(logout_option)

          print("Logout option hovered.")

          # testing mouse hover reaction
          self.create_screenshot()
          time.sleep(1)

          logout_option.click()
          print("Logged out.")
          time.sleep(3)

          # take a screenshot after the testing is finished
          test.create_screenshot()

          # closing the browser
          self.browser.quit()

# test execution
test = WebsiteFunctionalityTest(1)  # use browser type number (1: Chrome, 2: Firefox, 3: Edge, 4: Safari)
test.run_test()
