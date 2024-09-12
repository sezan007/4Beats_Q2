import pytest
from webdriver_manager import WebDriverManager
from page_objects.home_page import HomePage
import time

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    # Initialize WebDriver
    driver = WebDriverManager.get_driver()
    yield driver
    # Quit WebDriver after the tests
WebDriverManager.quit_driver()
driver = WebDriverManager.get_driver()
home_page = HomePage(driver)
home_page.load()
def test_amazon_captcha():

    home_page.solve_captcha()
    time.sleep(5)


def test_sign_in():
    home_page.sign_in("naimulsezan@gmail.com", "17963898310")
    time.sleep(5)
    # Assume captcha verification done before calling search
    # home_page.search("laptop")
    # time.sleep(10)
    # home_page.search("vape")
def test_amazon_search():
    home_page.search("laptop")
    time.sleep(5)

def test_amazon_music_click():
    # driver = WebDriverManager.get_driver()  # Reuse the existing WebDriver instance
    # home_page = HomePage(driver)
    # home_page.load()

    # Clicking the Amazon Music button
    home_page.click_amazon_music(driver)
    time.sleep(5)
def test_click_amazon_streaming_music():
    home_page.click_amazon_streaming_music(driver)
    time.sleep(5)
def test_click_amazon_podcast_music():
    home_page.click_amazon_podcast_music(driver)
    time.sleep(5)
def test_click_amazon_web_player():
    home_page.click_amazon_web_player(driver)
    time.sleep(5)

def test_click_amazon_books():
    home_page.click_amazon_books(driver)
    time.sleep(5)
def test_click_amazon_kindle_store():
    home_page.click_amazon_kindle_store(driver)
    time.sleep(5)
def test_click_amazon_kindle_unlimited():
    home_page.click_amazon_kindle_unlimited(driver)
    time.sleep(5)
def test_click_amazon_kindle_prime():
    home_page.click_amazon_kindle_prime(driver)
    time.sleep(5)
def test_click_amazon_sup():
    home_page.click_amazon_sup(driver)
    time.sleep(5)
def test_click_amazon_camera():
    home_page.click_amazon_camera(driver)
    time.sleep(5)
def test_click_amazon_car():
    home_page.click_amazon_car(driver)
    time.sleep(5)
def test_click_amazon_mobile():
    home_page.click_amazon_mobile(driver)
    time.sleep(5)
def test_click_amazon_headphone():
    home_page.click_amazon_headphone(driver)
    time.sleep(5)

def test_click_amazon_audio():
    home_page.click_amazon_audio(driver)
    time.sleep(5)

def test_click_amazon_office():
    home_page.click_amazon_office(driver)
    time.sleep(5)
def test_click_amazon_portable():
    home_page.click_amazon_office(driver)
    time.sleep(5)
def test_amazon_sign_out():

    # Assuming the user is already signed in
    home_page.sign_out(driver)
    time.sleep(5)

