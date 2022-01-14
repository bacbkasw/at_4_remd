from selenium import webdriver
import time


def test_1():


    link = "https://remd-dev.rt-eu.ru"
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
    """
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    browser = webdriver.Chrome(options=options)
        
    browser.get(link)
    browser.maximize_window()
    time.sleep(5)
    browser.quit()