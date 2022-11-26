from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

PROMISED_DOWN = 50
PROMISED_UP = 50
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
EMAIL = os.environ["EMAIL"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        self.driver.find_element(By.CSS_SELECTOR, '.js-start-test').click()
        time.sleep(45)
        result = self.driver.find_elements(By.CSS_SELECTOR, ".result-data-large")
        self.down = float(result[0].text)
        self.up = float(result[1].text)
        print(f"down: {self.down}\n up: {self.up}")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".css-4rbku5").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".r-30o5oe").send_keys(EMAIL, Keys.ENTER)
        time.sleep(2)
        try:
            username = self.driver.find_element(By.CSS_SELECTOR, 'input[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
            username.send_keys(USERNAME)
            time.sleep(2)
            username.send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(2)
        password = self.driver.find_element(By.CSS_SELECTOR, 'input[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        if self.down >= PROMISED_DOWN and self.up >= PROMISED_UP:
            tweet = "Appreciation to @PLDTHome for delivering the promised 50MBPS upload and download speeds."
        else:
            tweet = f"@PLDTHome, current download speed: {self.down} and upload speed: {self.up} are below promised 50MBPS speed."
        send_tweet = self.driver.find_element(By.CSS_SELECTOR, 'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
        send_tweet.send_keys(tweet)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]').click()
        time.sleep(15)