from selenium import webdriver
import time

link = "https://remd-dev.rt-eu.ru"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()
time.sleep(5)
browser.quit()