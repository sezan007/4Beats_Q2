# home_page.py
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class HomePage:
    CAPTCHA_FIELD = (By.ID, "captchacharacters")  # Locate the CAPTCHA input field
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button.a-button-text")  # Locate the Continue button
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.amazon.com")

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )

    def search(self, item):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(item)
        search_box.submit()

    def solve_captcha(self):
        """Prompt the user to enter the CAPTCHA and submit it."""
        captcha_value = input("Please enter the CAPTCHA value: ")

        # Find the CAPTCHA input field and enter the value
        captcha_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CAPTCHA_FIELD)
        )
        captcha_field.send_keys(captcha_value)  # Input the CAPTCHA

        # Find the Continue button and click it to submit the CAPTCHA form
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()

    def sign_in(self, email, password):
        # Navigate to the Amazon sign-in page
        sign_in_button = self.driver.find_element(By.ID, "nav-link-accountList")
        sign_in_button.click()

        # Input email/username
        email_input = self.driver.find_element(By.ID, "ap_email")
        email_input.clear()
        email_input.send_keys(email)

        # Click Continue
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

        # Now wait for the password field to be present
        try:
            password_input = self.driver.find_element(By.ID, "ap_password")
            password_input.clear()
            password_input.send_keys(password)

            # Click the Sign-In button
            sign_in_submit = self.driver.find_element(By.ID, "signInSubmit")
            sign_in_submit.click()

        except NoSuchElementException:
            print("Password field not found or page did not load correctly.")

    def click_amazon_music(self,driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH,"//div[text()='Amazon Music']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT,"Amazon Music Unlimited")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Amazon Music!")

        except Exception as e:
            print(f"Failed to click on Amazon Music: {e}")

        # Assuming driver is your singleton WebDriver instance
        # click_amazon_music_unlimited(driver)
        time.sleep(5)  # Wait after clicking to observe the result
    def click_amazon_streaming_music(self,driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH,"//div[text()='Amazon Music']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT,"Free Streaming Music")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Amazon Streaming Music!")

        except Exception as e:
            print(f"Failed to click on Streaming Amazon Music: {e}")

        # Assuming driver is your singleton WebDriver instance
        # click_amazon_music_unlimited(driver)
        time.sleep(5)  # Wait after clicking to observe the result


    def click_amazon_podcast_music(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Amazon Music']")

            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Podcasts")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Podcast")

        except Exception as e:
            print(f"Failed to click on podcast: {e}")

        # Assuming driver is your singleton WebDriver instance
        # click_amazon_music_unlimited(driver)
        time.sleep(5)  # Wait after clicking to observe the result

    def click_amazon_web_player(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Amazon Music']")

            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Open Web Player")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Amazon Web Player!")

        except Exception as e:
            print(f"Failed to click on Web Player: {e}")

        # Assuming driver is your singleton WebDriver instance
        self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
        self.wait_for_page_to_load()

        time.sleep(5)
    def click_amazon_books(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Kindle E-readers & Books']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Kindle Kids")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Amazon Books!")

        except Exception as e:
            print(f"Failed to click on Amazon Books: {e}")

        # Assuming driver is your singleton WebDriver instance

    def click_amazon_kindle_store(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Kindle E-readers & Books']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Kindle Books")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Kindle store!")

        except Exception as e:
            print(f"Failed to click on Kindle Books {e}")

        # Assuming driver is your singleton WebDriver instance

    def click_amazon_kindle_unlimited(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Kindle E-readers & Books']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Kindle Unlimited")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Kindle unlimited!")

        except Exception as e:
            print(f"Failed to click on Kindle unlimited {e}")

    def click_amazon_kindle_prime(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Kindle E-readers & Books']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Prime Reading")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Prime Reading!")
            self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on Prime Reading {e}")

    def click_amazon_sup(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Electronics']")
            amazon_music_element.click()
            time.sleep(3)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Accessories & Supplies")
            time.sleep(4)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Accessories &amp; Supplies!")
            # self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            # self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on PAccessories &amp; Supplies {e}")
    def click_amazon_camera(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Electronics']")
            amazon_music_element.click()
            time.sleep(3)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Camera & Photo")

            time.sleep(4)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Acamera and photo!")
            # self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            # self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on camera & photo {e}")
    def click_amazon_car(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Electronics']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Car & Vehicle Electronics")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Car & Vehicle Electronics!")
            # self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            # self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on Car & Vehicle Electronics {e}")
    def click_amazon_mobile(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Electronics']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Cell Phones & Accessories")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Cell Phones &amp; Accessories!")
            # self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            # self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on Cell Phones &amp; Accessories {e}")
    def click_amazon_gps(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Electronics']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "GPS & Navigation")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on GPS & Navigation!")
            # self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            # self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on GPS & Navigation {e}")

    def click_amazon_headphone(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Electronics']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Headphones")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Headphones!")
            # self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            # self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on Headphones {e}")
    def click_amazon_audio(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Electronics']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Home Audio")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Home Audio!")
            # self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            # self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on Home Audio {e}")

    def click_amazon_office(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Electronics']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Office Electronics")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Office Electronics!")
            # self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            # self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on Office Electronics {e}")

    def click_amazon_portable(self, driver):
        # Wait until the Amazon Music button is visible and clickable
        try:
            # Wait until the element is clickable
            music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            music.click()
            # music = self.driver.find_element(By.ID, "nav-hamburger-menu")
            # music.click()
            time.sleep(2)
            amazon_music_element = self.driver.find_element(By.XPATH, "//div[text()='Electronics']")
            amazon_music_element.click()
            time.sleep(2)

            amazon_music_unlimited = self.driver.find_element(By.LINK_TEXT, "Portable Audio & Video")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", amazon_music_unlimited)

            time.sleep(2)
            print("Clicked on Portable Audio & Video!")
            # self.driver.get("https://www.amazon.com")  # Redirect to Amazon homepage
            # self.wait_for_page_to_load()

        except Exception as e:
            print(f"Failed to click on Portable Audio & Video {e}")
    def sign_out(self,driver):
        # Hover over the "Account & Lists" menu
        account_list = self.driver.find_element(By.ID, "nav-link-accountList")
        actions = ActionChains(self.driver)
        actions.move_to_element(account_list).perform()

        # Wait until the "Sign Out" option is visible using the ID
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "nav-item-signout"))
        )

        # Click on the "Sign Out" button
        sign_out_button = self.driver.find_element(By.ID, "nav-item-signout")
        sign_out_button.click()