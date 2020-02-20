
# coding = utf-8
from selenium import webdriver
chrome_option = webdriver.ChromeOptions()
browser = webdriver.Chrome(options = chrome_option)
browser.get("https://www.baidu.com")