import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from User_Simulation import UserSimulation

# create an instance of the UsreSimulation class with the desired browser type (1: Chrome, 2: Firefox, 3: Edge, 4: Safari)
user_sim = UserSimulation(1)

# initialize the Selenium WebDriver
browser=user_sim.browser
browser.maximize_window()

mouse_hovering = ActionChains(browser)
wait = WebDriverWait(browser, 10)

# navigating to the menu
menu_button = user_sim.browser.find_element(By.XPATH, "/html/body/app/master-layout/div/baasic-header/header/div")
user_sim.hover_and_click(menu_button)
print("Navigated to the menu.")
user_sim.wait_for_seconds()

# user login on the website
user_sim.login("miksi23", "Winnetou210954")
time.sleep(3)

# navigating to album
latest_album_thumbnail=user_sim.browser.find_element(By.XPATH,"/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div[2]/div[1]")
user_sim.hover_and_click(latest_album_thumbnail)
user_sim.wait_for_seconds()

# find image elements with the given class
images = browser.find_elements(By. CLASS_NAME, "thumbnail__img")

# display HTML code and 'src' attribute for the first image
first_image = images[0]
html_code = first_image.get_attribute("outerHTML")

# extract URL from the style attribute
style_attribute = first_image.get_attribute("style")
start_url = style_attribute.find("url(") + 4
end_url = style_attribute.find(")")
image_url = style_attribute[start_url:end_url].strip("\"'")

print("HTML code of the image:")
print(html_code)

print("'src' attribute extracted from the style attribute:")
print(image_url)

# close the browser
browser.quit()