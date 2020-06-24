from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent']=("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")

driver = webdriver.PhantomJS(executable_path='/Users/apple/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs',desired_capabilities=dcap)
cusip = "037833100"

driver.get("https://investor.vanguard.com/search/?query="+cusip)


output = driver.find_element_by_xpath("/html/body/div[2]/div[2]/input[3]")
time.sleep(1)

print(output.get_attribute('value'))