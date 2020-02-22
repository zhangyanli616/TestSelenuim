
# coding = utf-8
from selenium import webdriver
chrome_option = webdriver.ChromeOptions()
browser = webdriver.Chrome(options = chrome_option)
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')

browser.get("https://www.baidu.com")


# wd = webdriver.Chrome('C:\\Users\\zhangyanli\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe')
# wd.get('https://www.baidu.com')