import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome, Edge, Firefox, Safari
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# initialize the Selenium WebDriver
browser= Chrome()
browser.maximize_window()

mouse_hovering = ActionChains(browser)

# open the website
browser.get('http://demo.baasic.com/angular/starterkit-photo-gallery/main')
time.sleep(3)

open_gallery_button = browser.find_elements(By.TAG_NAME, "svg")[1]
mouse_hovering.move_to_element(open_gallery_button).click().perform()
time.sleep(1)

def simulate_scroll_down(browser, scrolls, scroll_delay):
    scroll_element = browser.find_element(By.TAG_NAME, 'body')
    
    for _ in range(scrolls):
        # scroll down
        scroll_element.send_keys(Keys.PAGE_DOWN)
        time.sleep(scroll_delay)

def scroll_and_count_all_images(browser, scroll_delay, max_scrolls, output_file):
    scroll_element = browser.find_element(By.TAG_NAME, 'body')
    
    previous_images_count = len(browser.find_elements(By.CLASS_NAME, "thumbnail__img"))
    scrolls_done = 0

    with open(output_filename, "a") as output_file:  # open the file for appending data
        while scrolls_done < max_scrolls:
            # scroll down
            scroll_element.send_keys(Keys.PAGE_DOWN)
            time.sleep(scroll_delay)
            
            # store the image count after scrolling
            current_images_count = len(browser.find_elements(By.CLASS_NAME, "thumbnail__img"))
            
            # check for new images
            if current_images_count == previous_images_count:
                scrolls_done += 1
            else:
                scrolls_done = 0
            
            previous_images_count = current_images_count

            if scrolls_done == max_scrolls:
                # no new images after multiple scrolls, assume all images are displayed
                output_file.write("All images are displayed.\n")
                output_file.write("There are a total of " + str(current_images_count) + " images.\n\n")
                break

def test_thumbnail_image_urls(output_file):
  
    # find image elements with the given class
    image_elements = browser.find_elements(By.CLASS_NAME,"thumbnail__img")

    with open(output_filename, "a") as output_file:  # Open the file for appending data
        for index, image in enumerate(image_elements):
            try:
                # attempt to access the 'style' attribute of the image element
                image_style = image.get_attribute('style')
                
                # check if the background-image URL exists
                if "background-image" in image_style:
                    # find the index where the URL starts (after 'url("')
                    image_url_start = image_style.index('url("') + 5
                    # find the index where the URL ends (after 'image_url_start' and before '")' )
                    image_url_end = image_style.index('")', image_url_start)
                    # extract the actual image URL using slicing
                    image_url = image_style[image_url_start:image_url_end]
                    output_file.write(f"Image {index + 1}: {image_url}\n")
                else:
                    output_file.write(f"Image {index + 1} - No image URL found\n")
            except NoSuchElementException:
                output_file.write(f"Image {index + 1} - Element not found\n")

# open the file at the beginning of the program
output_filename = "Output.txt"

# simulate scroll down
scroll_and_count_all_images(browser, 3, 10, output_filename)

# test and record thumbnail image URLs
test_thumbnail_image_urls(output_filename)

# close the browser
browser.quit()