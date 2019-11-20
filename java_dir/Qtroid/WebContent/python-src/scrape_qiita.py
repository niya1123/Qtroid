from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import connect_mysql

class QiitaGetRanking():
    """
    Qiitaからランキングエータを取得し, mysqlに登録するクラス.
    """

    def get_tag_ranking(self, browser: webdriver) -> dict:
        """
        Qiitaからタグランキングに関する情報を取得する関数.

        Returns
        -------
        tag_ranking_data: dict
            タグランキングを収めた辞書オブジェクト.
        """
        html = browser.page_source.encode('utf-8')
        soup = BeautifulSoup(html, "html.parser")
        ra_tag_names = soup.find_all(class_='ra-Tag_name pr-1')[:5]
        tag_ranking_data = {}
        for i, ra_tag_name in enumerate(ra_tag_names):
            tag_ranking_data[i+1] = [ra_tag_name.text, 
            'https://qiita.com/tags/%s'%(ra_tag_name.text.lower())]
        return tag_ranking_data
    
    def get_trend_data(self, tag_ranking_data: dict, browser: webdriver):
        trend_data = {}

        for ranking in list(tag_ranking_data.keys()):
            browser.get(tag_ranking_data[ranking][1])
            tag_trend_html = browser.page_source.encode('utf-8')
            soup = BeautifulSoup(tag_trend_html, "html.parser")
            trends = soup.find_all(class_='tst-ArticleBody_title')[:6]
            trend_detail_list = []
            for i, trend in enumerate(trends):
                trend_detail_list.append({i+1: [trend.text, 'https://qiita.com%s'%(trend.get('href'))]})
            trend_data[tag_ranking_data[ranking][0]] = trend_detail_list
        return trend_data



if __name__ == "__main__":
    """
    main文. browserはhtmlの取得が終わり次第閉じること.エラーが出てきたときも同様.
    """
    try:
        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        print("start scrape")
        browser.get('https://qiita.com')
        WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)
        print("generate object")
        qgr = QiitaGetRanking()
        ranking_data = qgr.get_tag_ranking(browser)
        trend_data = qgr.get_trend_data(ranking_data, browser)
        # print(list(trend_data.values())[0][0].keys())
        print("connect to mysql")
        cm = connect_mysql.ConnectMySQL()
        cm.register_tag_ranking(ranking_data)
        cm.register_trend_data(trend_data)
        cm.connection_closed()
        print("done")
    except:
        browser.close()
        browser.quit()
    finally:
        browser.close()
        browser.quit()