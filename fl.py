from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent']=("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")

driver = webdriver.PhantomJS(executable_path='/Users/apple/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs',desired_capabilities=dcap)
driver.get("https://www.google.com/flights")



# loc_from = driver.find_element_by_class_name("flt-input gws-flights-form__input-container gws-flights__flex-box gws-flights-form__airport-input gws-flights-form__empty gws-flights-form__swapper-right")
# loc_from.send_keys('New York')


loc_to = driver.find_element_by_name("/html/body/div[2]/div[2]/div/div[2]/div[3]/div/jsl/div/div[2]/main[1]/div[4]/div/div[3]/div/div[2]/div[2]")
loc_to.send_keys('Beijing')
loc_to.send_keys(Keys.RETURN)


time.sleep(3)

driver.save_screenshot('flight.png')
print("Google Search Complete")


