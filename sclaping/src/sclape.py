# -*- coding: utf-8 -*-
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys


def chrome():
    driver = webdriver.Chrome(executable_path='/usr/local/git_local/python_study/scraping/etc/chromedriver')
    conf_f = open('../etc/account.conf', 'r')
    for value in conf_f:
        key = value.rstrip().split(',')[0]
        if key == 'ID':
            id = value.rstrip().split(',')[1]
        elif key == 'PASS':
            password = value.rstrip().split(',')[1]

    try:
        driver.get('https://www.instagram.com/')
        # facebookでログイン
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button').click()
        driver.find_element_by_id('email').send_keys(id)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('loginbutton').click()

        time.sleep(3)
        # キーワードで検索
        keyword = '焼肉'
        driver.get('https://www.instagram.com/explore/tags/' + keyword + '/')
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[3]/a').click()

        print 'a'

        # //*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]
        # //*[@id="react-root"]/section/main/article/div[2]/div[1]/div[2]


    except Exception as e:
        print e
    finally:
        driver.close()


if __name__ == '__main__':
    start = time.time()
    print 'start :', start
    # file_no = '2'
    # file_no = sys.argv[1]
    chrome()
