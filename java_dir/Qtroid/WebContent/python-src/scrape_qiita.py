from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from lxml.html import fromstring, tostring
import time
import os

class QiitaGetRanking():
    """
    Qiitaからランキングエータを取得し, mysqlに登録するクラス.
    """

    def __init__(self, browser: webdriver):
        browser.get('https://qiita.com')
        self.encoding = 'utf-8'
        self.html = browser.page_source.encode(self.encoding)

    def get_tag_ranking(self):
        soup = BeautifulSoup(self.html, "html.parser")
        ra_tag_names = soup.find_all(class_='ra-Tag_name pr-1')
        ranking_data = {}
        for i, ra_tag_name in enumerate(ra_tag_names):
            ranking_data[i+1] = ra_tag_name.text.encode(self.encoding)

if __name__ == "__main__":
    try:
        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)
        qgr = QiitaGetRanking(browser)
        browser.close()
        browser.quit()
        qgr.get_tag_ranking()
    except:
        browser.close()
        browser.quit()