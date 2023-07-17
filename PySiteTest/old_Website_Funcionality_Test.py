from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
type_of_browser = 1;
if(type_of_browser == 1):
    browser = webdriver.Chrome()
elif(type_of_browser == 2):
    browser = webdriver.Firefox()
elif(type_of_browser == 3):
    browser = webdriver.Edge()
else:
    print("Enter valid browser number; 1, 2 or 3")

browser.get('http://demo.baasic.com/angular/starterkit-photo-gallery/main')
mouse_hovering= ActionChains(browser)
#search field validation
search_field=browser.find_element(By.NAME, "search")
mouse_hovering.move_to_element(search_field).click().perform()
time.sleep(3)
search_field.send_keys("pas")
time.sleep(3)
search_field.send_keys(Keys.RETURN)
time.sleep(3)
#search results verification
search_result=browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-search-result-route/baasic-photo-list/div/div[2]/span/div[1]")
mouse_hovering.move_to_element(search_result).click().perform()
time.sleep(3)
#exiting search result
exit_search_result=browser.find_element(By.XPATH,"//button[@type='button']")
exit_search_result.click()
time.sleep(3)
#dropdown menu button validation
menu_buton=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
mouse_hovering.move_to_element(menu_buton).click().perform()
time.sleep(1)
#dropdown home button validation
menu_buton=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
mouse_hovering.move_to_element(menu_buton).click().perform()
time.sleep(1)
logo_button=browser.find_element(By.TAG_NAME, "use")
mouse_hovering.move_to_element(logo_button).click().perform()
time.sleep(1)
#navigating to the menu
menu_buton=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
mouse_hovering.move_to_element(menu_buton).click().perform()
time.sleep(3)
#login form validation
login_option=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[2]/span")
mouse_hovering.move_to_element(login_option).click().perform()
time.sleep(3)
username_field=browser.find_element(By.NAME, "username")
username_field.send_keys("miksi23")
time.sleep(1)
password_field=browser.find_element(By.NAME, "password")
password_field.send_keys("Winnetou210954")
time.sleep(1)
login_button=browser.find_elements(By.TAG_NAME, "button")[0]
login_button.click()
time.sleep(3)
#album creation
create_album_button=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div/div[2]/button")
create_album_button.click()
time.sleep(3)
album_name=browser.find_element(By.NAME,"albumName")
album_name.send_keys("moj prvi album")
time.sleep(1)
album_description=browser.find_element(By.NAME,"albumDescription")
album_description.send_keys("moja prva slika")
time.sleep(1)
save_album_button=browser.find_elements(By.TAG_NAME,"button")[1]
save_album_button.click()
time.sleep(3)
#cover photo upload
upload_cover_photo= browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-album-create-route/div/div/div/div[1]")
upload_cover_photo.click()
time.sleep(3)
upload_cover_input=browser.find_element(By.ID,"photoInput")
cover_photo_path="C:\\Users\Mira\Desktop\santa-monica-pier.jpg"
upload_cover_input.send_keys(cover_photo_path)
upload_button=browser.find_element(By.XPATH,"//button[@type='submit']")
upload_button.click()
browser.implicitly_wait(10)
#image upload
image_upload=browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
mouse_hovering.move_to_element(image_upload).click().perform()
time.sleep(3)
upload_photo_button=browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[3]/button")
upload_photo_button.click()
time.sleep(3)
upload_image_input=browser.find_element(By.ID, "photoInput")
image_path="C:\\Users\Mira\Desktop\architecture-1280.jpg"
upload_image_input.send_keys(image_path)
upload_button=browser.find_element(By.XPATH,"//button[@type='submit']")
upload_button.click()
browser.implicitly_wait(10)
#image deleting
image_deleting=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]")
mouse_hovering.move_to_element(image_deleting).click().perform()
time.sleep(1)
delete_image_button=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[2]/div/span/div[1]/div[3]/div/button")
mouse_hovering.move_to_element(delete_image_button).click().perform()
time.sleep(3)
confirm_delete1=browser.find_element(By.XPATH, "//button[@class='btn btn--med btn--warning']")
confirm_delete1.click()
time.sleep(3)
#returning to albums
go_back_to_albums_button=browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/baasic-photo-list-route/baasic-album-detail/div/div[1]/div[1]/button")
go_back_to_albums_button.click()
time.sleep(3)
#album deleting
delete_album=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
mouse_hovering.move_to_element(delete_album).perform()
delete_album_button=browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]/span/div[1]/div[4]/button")
delete_album_button.click()
delete_album_confirm=browser.find_element(By.XPATH,"/html/body/app/master-layout/modal-component/div/div[2]/div[3]/button[1]")
delete_album_confirm.click()
#navigating to the menu
menu_buton=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
mouse_hovering.move_to_element(menu_buton).click().perform()
time.sleep(1)
#profile option verification
profile_button=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[1]/span")
mouse_hovering.move_to_element(profile_button).perform()
time.sleep(1)
profile_button.click()
time.sleep(3)
#navigating to the menu
menu_buton=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
mouse_hovering.move_to_element(menu_buton).click().perform()
time.sleep(3)
#create album option verification
create_album_option=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/li[2]/span")
mouse_hovering.move_to_element(create_album_option).perform()
time.sleep(1)
create_album_option.click()
time.sleep(3)
#navigating to the menu
menu_buton=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
mouse_hovering.move_to_element(menu_buton).click().perform()
time.sleep(3)
#logout option verification
logout_option=browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/nav/div/ul/baasic-logout/li/span")
mouse_hovering.move_to_element(logout_option).perform()
time.sleep(1)
logout_option.click()
time.sleep(5)
browser.quit()
