import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
url = 'https://www.zerohedge.com/'

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent']=("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")

driver = webdriver.PhantomJS(executable_path='/Users/apple/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs',desired_capabilities=dcap)
driver.get(url)
time.sleep(1)

for idx in range(3):
    article_xpath = '/html/body/div[1]/div/div/div[2]/div/main/div/div/div/div/div/div/div[{}]/article/h2/a'.format(idx+1)
    elem_sub = driver.find_element_by_xpath(article_xpath)
    elem_sub.click()
    time.sleep(3)
    driver.maximize_window()
    current_time = str(datetime.now())
    driver.save_screenshot(current_time[:10] + '_' + str(idx) + '.png')
    driver.back()
driver.close()
