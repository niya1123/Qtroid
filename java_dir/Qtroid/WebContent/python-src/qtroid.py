from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from time import sleep
import register_mysql

class QiitaGetRanking():
    """
    Qiitaからランキングエータを取得し, mysqlに登録するクラス.
    """

    def __init__(self):
        self.browser = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    
    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def get_tag_ranking(self) -> dict:
    # def get_tag_ranking(self, browser:webdriver) -> dict:
        """
        Qiitaからタグランキングに関する情報を取得する関数.

        Returns
        -------
        tag_ranking_data: dict
            タグランキングを収めた辞書オブジェクト.
        """
        browser = self.browser
        browser.get('https://qiita.com')
        WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)
        html = browser.page_source.encode('utf-8')
        soup = BeautifulSoup(html, "html.parser")
        ra_tag_names = soup.find_all(class_='ra-Tag_name pr-1')[:5]
        tag_ranking_data = {}
        for i, ra_tag_name in enumerate(ra_tag_names):
            tag_ranking_data[i+1] = [ra_tag_name.text, 
            'https://qiita.com/tags/%s'%(ra_tag_name.text.lower())]
        return tag_ranking_data
    
    def get_trend_data(self, tag_ranking_data: dict):
    # def get_trend_data(self, tag_ranking_data: dict, browser:webdriver):
        browser = self.browser
        trend_data = {}

        for ranking in list(tag_ranking_data.keys()):
            browser.get(tag_ranking_data[ranking][1])
            WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)
            tag_trend_html = browser.page_source.encode('utf-8')
            soup = BeautifulSoup(tag_trend_html, "html.parser")
            trends = soup.find_all(class_='tst-ArticleBody_title')
            like_count = soup.find_all(class_='tst-ArticleBody_likeCount')
            trend_detail_list = []
            for i, trend in enumerate(trends):
                trend_detail_list.append({i+1: [trend.text, int(like_count[i].text), 
                'https://qiita.com%s'%(trend.get('href'))]})
            trend_data[tag_ranking_data[ranking][0]] = trend_detail_list
        return trend_data
    
    def get_article_data(self, trend_data):
        browser = self.browser
        article_data = {}
        print("start")
        for tag_name in list(trend_data.keys()):
            for trend_article_data in list(trend_data[tag_name]):
                browser.get(trend_article_data.get( list(trend_article_data.keys())[0] )[2])
                sleep(2)
                WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)
                article_html = browser.page_source.encode('utf-8')
                soup = BeautifulSoup(article_html, "html.parser")
                article_body = soup.find(class_="it-MdContent")
                if article_body is None:
                    pass
                link_tag_a = article_body.find_all("a")
                # sleep(1)
                hrefs = []
                for a in link_tag_a:
                    link = a.get("href")
                    if link is None:
                        pass
                    elif link.startswith("#"):
                        pass
                    elif "qiita-image-store" in link:
                        pass
                    else:
                        hrefs.append(link)
                #    hrefs.append(a.get("href"))
                # hrefs = [s for s in hrefs if s.startswith("http")]
                # hrefs = [s.get("href") for s in link_tag_a if s.get("href").startswith("h")]
                article_data[trend_article_data.get( list(trend_article_data.keys())[0] )[0]] = hrefs

        return article_data

if __name__ == "__main__":
    """
    main文. browserはhtmlの取得が終わり次第閉じること.エラーが出てきたときも同様.
    """
    
    # print("create browser")
    # browser = webdriver.Remote(
    #     command_executor='http://selenium-hub:4444/wd/hub',
    #     desired_capabilities=DesiredCapabilities.CHROME)
    print("generate object")
    qgr = QiitaGetRanking()
    print("start scrape")
    # ranking_data = qgr.get_tag_ranking(browser)
    # trend_data = qgr.get_trend_data(ranking_data, browser)
    ranking_data = qgr.get_tag_ranking()
    trend_data = qgr.get_trend_data(ranking_data)
    article_data = qgr.get_article_data(trend_data)
    qgr.close_browser()
    # browser.close()
    # browser.quit()
    print("connect to mysql")
    rm = register_mysql.RegisterMySQL()
    rm.register_tag_ranking(ranking_data)
    rm.register_trend_data(trend_data)
    rm.register_article_data(article_data)
    rm.connection_closed()
    print("done")
    