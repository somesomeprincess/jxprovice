import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


with open('ming.json', 'r') as f:
    name_json = json.load(f)
def close_the_tishi(driver):
    close = driver.find_element(By.CSS_SELECTOR, 'div#pop_main a')

    close.click()


def login(driver, usrname, password):
    username = driver.find_element(By.ID, 'username')
    username.clear()
    username.send_keys(usrname)
    pwd = driver.find_element(By.ID, 'password')
    pwd.clear()
    pwd.send_keys(password)
    login = driver.find_element(By.ID, 'submit')
    login.click()


def close_popup(driver, name_json):
    try:
        WebDriverWait(driver, 5, 1).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, name_json['Home']['Popup_window'])), '弹窗失败')
        driver.find_element(By.CSS_SELECTOR, name_json['Home']['Popup']).close()
        WebDriverWait(driver, 5, 1).until_not(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, name_json['Home']['Popup_window'])), '关闭弹窗失败')
    except:
        pass

def register(self, name, email, mobile, org):
    self.driver.find_element(By.CSS_SELECTOR, self.name_json['Home']['Register']).click()
    WebDriverWait(self.driver, 10, 1).until(EC.title_contains('注册向导'), '注册跳转失败')
    WebDriverWait(self.driver, 10, 1).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, self.name_json['Register']['Identity'])))
    self.driver.find_element(By.CSS_SELECTOR, self.name_json['Register']['Identity']).click()
    self.driver.find_element(By.CSS_SELECTOR, self.name_json['Register']['Agree_zhuanjia']).click()
    self.driver.find_element(By.CSS_SELECTOR, self.name_json['Register']['zhuangjia_next']).click()
    WebDriverWait(self.driver, 10, 1).until(EC.title_contains('评议人注册信息'), '填写资料跳转失败')
    self.driver.find_element(By.CSS_SELECTOR, self.name_json['Register']['zhname']).send_keys(name)
    self.driver.find_element(By.CSS_SELECTOR, self.name_json['Register']['email']).send_keys(email)
    self.driver.find_element(By.CSS_SELECTOR, self.name_json['Register']['mobile']).send_keys(mobile)
    self.driver.find_element(By.CSS_SELECTOR, self.name_json['Register']['mobile']).send_keys(org)
    self.driver.find_element(By.CSS_SELECTOR, self.name_json['Register']['submitbtn']).click()


def open_url(self, url):
    self.driver.get(url)
