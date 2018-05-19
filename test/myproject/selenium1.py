from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
pageSource = driver.page_source 
bsObj = BeautifulSoup(pageSource) 
print(bsObj.find(id="content").get_text())

driver.close()
