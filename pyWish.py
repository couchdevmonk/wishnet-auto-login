# Used to import the webdriver from selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from urllib.request import urlopen
import time
import datetime
import os


# Get the path of chromedriver which you have installed
def startBot(username, password, url):
    path = "path-to-chromedriver"
    # giving the path of chromedriver to selenium webdriver
    options = Options()
    options.add_argument('--ignore-certificate-errors-spki-list') # wishnet login page doesn't have proper ssl certs
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-gpu')   # to run headless chrome
    options.add_argument('--headless')  # to run headless chrome
    driver = webdriver.Chrome(service=Service(path), options=options)

    # opening the website in chrome.
    driver.get(url)

    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element(By.NAME, "Username").send_keys(username)
    # find the password by inspecting on password input
    driver.find_element(By.NAME, "Password").send_keys(password)

    # click on submit
    driver.find_element(By.ID, "submit_btn").click()

def internet_on():
    try:
        response = urlopen('https://www.google.com',timeout=10)
        return True
    except:
        return False



# Driver Code
# Enter below your login credentials
username = "your-username"
password = "your-password"

# URL of the login page of site which you want to automate login.
url = "your-wishnet-login-url"

# Call the function every 1 secs
while True:
    if internet_on() == False:
        startBot(username, password, url)
        log = open("log.txt", "a")
        log.write("[{}]: Successfully logged in.\n".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
        log.close()
    time.sleep(1)
