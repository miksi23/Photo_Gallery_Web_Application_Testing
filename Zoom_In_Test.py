import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inicijalizacija Selenium drajvera (koristimo Chrome drajver ovde)
driver = webdriver.Chrome()

# initialize the Selenium WebDriver
browser = webdriver.Chrome()
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

try:
    # Pronalaženje svih slika u galeriji
    images = browser.find_elements(By.CLASS_NAME, "thumbnail__img")

    if images:
        # Simulirajte povećanje prvih nekoliko slika (npr. prvih 5)
        for i in range(min(5, len(images))):
            image = images[i]
            # Kliknite na sliku da je otvorite
            image.click()

            # Sačekajte da se povećana slika pojavi
            time.sleep(1)
            
            # Provera da li je povećana slika prikazana
            zoomed_image = browser.find_element(By.CLASS_NAME, "image--primary")
            assert zoomed_image.is_displayed(), "Povećana slika se nije prikazala kako se očekivalo."
            
            # Simulacija otvaranja slike u novom prozoru mišem
            action = ActionChains(browser)
            action.context_click().perform()
            time.sleep(1)
            
            # Simulacija povećanja slike unutar novog prozora
            zoom_in_button = browser.find_element(By.CLASS_NAME, "zoom-in-button")
            zoom_in_button.click()
            assert zoom_in_button.is_displayed(), "Povećana slika u novom prozoru se nije prikazala kako se očekivalo."
            time.sleep(1)

            # Zatvaranje novog prozora sa povećanom slikom
            browser.close()
            
            # Povratak na prethodni prozor (galerija)
            browser.switch_to.window(browser.window_handles[0])

    else:
        print("Nema slika u galeriji.")

except AssertionError as ae:
    print("Greška pri povećanju slike:", ae)

except Exception as e:
    print("Došlo je do greške:", e)

simulate_scroll_down(browser, 10, 0.5)