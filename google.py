from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent']=("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")

driver = webdriver.PhantomJS(executable_path='/Users/apple/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs',desired_capabilities=dcap)
driver.get("https://google.com")

key_word = "ithaca"
google_search = driver.find_element_by_name("q")
google_search.send_keys(key_word)
google_search.send_keys(Keys.RETURN)
time.sleep(1)

driver.save_screenshot('{}.png'.format(key_word))
print("Google Search Complete")