"""Блок импорта"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import pytest
# import testit
import os

"""Здесь константы, логины, пароли, явки"""

# link = "https://remd-dev.rt-eu.ru"  # линк на дев стенд
link = "https://remd.rt-eu.ru"  # линк на тест стенд
username_locator = 'username'
password_locator = 'password'
submit_locator = 'kc-login'
# adm_stp_name = '069-257-426 97'
# adm_stp_passw = 'bynfyn'
# adm_fu_name = "240-811-207 19"
# adm_fu_passw = "123456"
# adm_ru_name = "610-000-003 65"
# adm_ru_passw = "654321"
# adm_mo_name = "896 893 697 31"
# adm_mo_passw = "112233"

"""Основные функции, многократно используемые в тестах"""


def delete_cache():
    driver = webdriver.Chrome("c:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData')  # for old chromedriver versions use cleardriverData
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3)  # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER)  # confirm
    actions.perform()
    time.sleep(5)  # wait some time to finish
    driver.close()  # close this tab
    driver.switch_to.window(driver.window_handles[0])  # switch back


def autorisation(user, passw):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser = webdriver.Chrome(options=options)
    browser.delete_all_cookies()
    # delete_cache()
    browser.get(link)
    browser.maximize_window()
    browser.find_element(By.ID, username_locator).send_keys(user)
    browser.find_element(By.ID, password_locator).send_keys(passw)
    # browser.implicitly_wait(10)
    browser.find_element(By.ID, submit_locator).click()
    try:
        browser.find_element(By.XPATH, "//div/input").click()
        time.sleep(5)
    except NoSuchElementException:
        time.sleep(3)
    return browser


# @testit.externalID('Smoke login STP')
# @testit.displayName('Тест вход СТП')
@pytest.mark.smoke
def test_login_STP_web_positive_():
    adm_stp_name = os.environ['adm_stp_name']
    adm_stp_passw = os.environ['adm_stp_passw']

    try:
        browser = autorisation(adm_stp_name, adm_stp_passw)
        time.sleep(3)
        assert "Главная" in browser.title
        print(' Авторизация СТП удачно - открыта страница: ', browser.title, end='')

    finally:
        time.sleep(5)
        browser.quit()


# @testit.externalID('Smoke login FU admin')
# @testit.displayName('Тест вход админ ФУ')
@pytest.mark.smoke
def test_login_adm_fu_web_positive_():
    try:
        adm_fu_name = os.environ['adm_fu_name']
        adm_fu_passw = os.environ['adm_fu_passw']
        browser = autorisation(adm_fu_name, adm_fu_passw)
        time.sleep(3)
        assert "Главная" in browser.title
        print(' Авторизация Адм. фед. уровня удачно - открыта страница: ', browser.title, end='')
    finally:
        time.sleep(3)
        browser.quit()


# @testit.externalID('Smoke login RU admin')
# @testit.displayName('Тест вход админ РУ')
@pytest.mark.smoke
def test_login_adm_reg_web_positive_():
    try:
        adm_ru_name = os.environ['adm_ru_name']
        adm_ru_passw = os.environ['adm_ru_passw']
        browser = autorisation(adm_ru_name, adm_ru_passw)
        time.sleep(3)
        assert "Главная" in browser.title
        print(' Авторизация Адм. рег. уровня удачно - открыта страница: ', browser.title, end='')
    finally:
        time.sleep(3)
        browser.quit()


# @testit.externalID('Smoke login MO admin')
# @testit.displayName('Тест вход админ МО')
@pytest.mark.smoke
def test_login_adm_mo_web_positive_():
    try:
        adm_mo_name = os.environ['adm_mo_name']
        adm_mo_passw = os.environ['adm_mo_passw']
        browser = autorisation(adm_mo_name, adm_mo_passw)
        time.sleep(3)
        assert "Главная" in browser.title
        print(' Авторизация Адм. мед. организации удачно - открыта страница: ', browser.title, end='')

    finally:
        time.sleep(3)
        browser.quit()
