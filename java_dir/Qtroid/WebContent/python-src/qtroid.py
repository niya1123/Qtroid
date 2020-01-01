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
            tag_ranking_data[i+1] = [ra_tag_name.text.lower(), 
            'https://qiita.com/tags/%s'%(ra_tag_name.text.lower())]
        return tag_ranking_data
    
    def get_trend_data(self, tag_urls: list) -> dict:
        """
        Qiitaのトレンドランキングから記事の情報を取得する関数.

        Returns
        -------
        trend_data: dict
            トレンドの記事のデータを収めた辞書オブジェクト.
        """
        browser = self.browser
        trend_data = {}
        for tag_url in tag_urls:
            browser.get(tag_url)
            WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)
            tag_trend_html = browser.page_source.encode('utf-8')
            soup = BeautifulSoup(tag_trend_html, "html.parser")
            trends = soup.find_all(class_='tst-ArticleBody_title')
            like_count = soup.find_all(class_='tst-ArticleBody_likeCount')
            trend_detail_list = []
            for i, trend in enumerate(trends):
                trend_detail_list.append({i+1: [trend.text, int(like_count[i].text), 
                'https://qiita.com%s'%(trend.get('href'))]})
            trend_data[tag_url.split("/")[-1]] = trend_detail_list
        return trend_data
    
    def get_article_data(self, trend_datas: dict):
        browser = self.browser
        article_data = {}
        print("start")
        
        for tag_name in list(trend_datas.keys()):
            browser.get(trend_datas.get(tag_name))
            WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)
            article_html = browser.page_source.encode('utf-8')
            soup = BeautifulSoup(article_html, "html.parser")
            article_body = soup.find(class_="it-MdContent")
            link_tag_a = article_body.find_all("a")
            hrefs = []
            for a in link_tag_a:
                link = a.get("href")
                hrefs.append(link)
            article_data[tag_name] = hrefs
        return article_data

if __name__ == "__main__":
    """
    main文. browserはhtmlの取得が終わり次第閉じること.エラーが出てきたときも同様.
    """
    print("generate object")
    print("start scrape")
    qgr = QiitaGetRanking()
    rm = register_mysql.RegisterMySQL()
    try:

        # ランキングデータの取得
        ranking_data = qgr.get_tag_ranking()
        # DBにランキングデータを登録
        rm.register_tag_ranking(ranking_data)
        
        # DBからtagのurlを取得
        tag_urls = rm.get_tag_urls()
        # タグランキングのトレンドデータを取得
        trend_data = qgr.get_trend_data(tag_urls)
        # DBにトレンドデータを登録
        rm.register_trend_data(trend_data)

        # DBからトレンドのurlを取得
        trend_urls = rm.get_trend_datas()
        # トレンド記事のデータを取得
        article_data = qgr.get_article_data(trend_datas)
        # DBにトレンド記事のデータを登録
        rm.register_article_data(article_data)

        # browserの閉じ
        qgr.close_browser()

        # DBのコネクション閉じ
        rm.connection_closed()
        print("done")
    except:
        qgr.close_browser()
    