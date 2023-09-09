import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class AlbumPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def upload_photo(self, photo_path, photo_description):
        # simulates uploading a photo to the website
        # enter the photo path into the upload image input field
        upload_image_input = self.browser.find_element(By.ID, "photoInput")
        upload_image_input.send_keys(photo_path)
        time.sleep(3)

        # enter the photo path into the upload image input field
        image_description = self.browser.find_element(By.ID, "photoDescription")
        image_description.send_keys(photo_description)
        time.sleep(1)
        
        # click on the upload button to upload the photo
        upload_button = self.browser.find_element(By.XPATH, "//button[@type='submit']")
        upload_button.click()
        print("Successfully uploaded the image.")

        # add waiting time after the image loads
        self.browser.implicitly_wait(10)
        time.sleep(3)  # additional waiting time after the image loads

    def delete_photo(self):

        confirm_delete = self.browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--warning']")
        confirm_delete.click()
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
        time.sleep(3)

        # click on the save album button to create the album
        save_album_button = self.browser.find_elements(By.TAG_NAME, "button")[1]
        save_album_button.click()
        time.sleep(3)

    def delete_album(self):

        confirm_album_delete=self.browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--warning']")
        confirm_album_delete.click()
        self.browser.implicitly_wait(10)
        print("Successfully deleted the latest album.")
        time.sleep(3)
        