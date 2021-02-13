import enum
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import configparser as cfg

class Flipkart_Scrapper():
    def __init__(self, credFileName):
        self.config = credFileName
        self.email, self.password, self.base_url, self.growth_url = self.read_creds()

    def read_creds(self):
        parser = cfg.ConfigParser()
        parser.read(self.config)
        return parser.get('credentials', 'email'), parser.get('credentials', 'password'), parser.get('credentials', 'base_url'), parser.get('credentials', 'growth_tab_url')

    def sleeper(self, secs):
        print("Sleeping for {} sec...".format(secs))
        time.sleep(secs)

    def scrape(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        self.sleeper(5)
        inputBox = driver.find_element_by_xpath("//input[@placeholder='Enter your username OR Phone Number OR Email']")
        self.sleeper(2)
        inputBox.send_keys(self.email)
        self.sleeper(2)
        next_btn = driver.find_element_by_xpath("//span[text()='Next']")
        next_btn.click()
        self.sleeper(2)
        passBox = driver.find_element_by_xpath("//input[@placeholder='Enter password']")
        self.sleeper(2)
        passBox.send_keys(self.password)
        self.sleeper(2)
        loginBtn = driver.find_element_by_xpath("//span[text()='Login']")
        loginBtn.click()
        self.sleeper(6)
        driver.get(self.growth_url)
        self.sleeper(4)
        salesInRupees = driver.find_element_by_xpath("//div[text()='Net Sales in Rupees >']")
        salesInRupees.click()
        self.sleeper(4)
        downloaded_report = False
        while(not downloaded_report):
            failed = False
            try:
                dnldReportBtn = driver.find_element_by_xpath("//button[text()='Download Report']")
                dnldReportBtn.click()
                print('Trying to Download Report!!')
                self.sleeper(10)
            except:
                failed = True
            if failed:
                driver.navigate().refresh()
                continue
            else:
                downloaded_report = True
        # if this fails
        self.sleeper(50)
        # Job Done! - Close Chrome
        # driver.quit()

