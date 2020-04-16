from selenium import webdriver
import time
import os
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dirpath = os.getcwd()

driver = webdriver.Chrome(
    executable_path=r"{}\chromedriver.exe".format(dirpath))

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("disable-infobars")
options.add_argument("--allow-file-access-from-files")
options.add_argument("--allow-file-access")
options.add_argument("--allow-cross-origin-auth-prompt")
options.add_argument("--disable-web-security")

driver = webdriver.Chrome(options=options)
url = "https://www.youtube.com/feed/trending/?gl=US"
driver.maximize_window()
driver.get(url)
wait = WebDriverWait(driver, 10)

def get_all_titles():
    WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_xpath("//a[@id='video-title']")) > 0)
    playlist_titles = driver.find_elements_by_xpath("//a[@id='video-title']")
    for playlist_title in playlist_titles:
        print(playlist_title.get_attribute("title"))
        print(playlist_title.get_attribute("aria-label"))
        print()

def get_all_():
    WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_xpath("//span[@class='style-scope ytd-video-meta-block']")) > 0)
    playlist_titles = driver.find_elements_by_xpath("//span[@class='style-scope ytd-video-meta-block']")
    for playlist_title in playlist_titles:
        print(playlist_title.text)
        print()
        # driver.find_elements_by_xpath("//span[@class='style-scope ytd-video-meta-block']")[0].text

try:
    get_all_titles()
    get_all_()
    import pdb; pdb.set_trace()

except Exception as ex:
    print(ex)
finally:
    driver.quit()






