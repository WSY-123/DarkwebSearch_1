# 使用搜索引擎在明网检索暗网域名
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, \
    WebDriverException,TimeoutException,NoSuchElementException
from time import sleep
import random

data = open("./darkwebSearch.txt",'w+',encoding='utf-8')
driver = webdriver.Chrome()
driver.implicitly_wait(10)

keyWords = ['site:onion.sh', 'site:onion.case', 'site:onion.best',
            'site:onion.guide', 'site:onion.run']

def findUrl(url,data):
    '''
    从搜索结果中找出暗网网页url
    '''
    driver.get(url)
    linklist = driver.find_elements_by_xpath('//*[@class="iUh30 tjvcx"]')
    for item in linklist:
        data.write(item.text+'\n')

for i in range(5):
    # 搜索
    driver.get('https://www.google.com/')
    ele = driver.find_element_by_name('q')
    ele.send_keys(keyWords[i])
    ele.submit()
    while(1):
        currentPageUrl = driver.current_url
        try:
            findUrl(currentPageUrl,data)
            time = random.randint(50,75)
            sleep(time)
            ele = driver.find_element_by_id("pnnext")
            ele.click()
        except NoSuchElementException:
            break

data.close()