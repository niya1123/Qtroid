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

    def __init__(self, browser: webdriver):
        """
        デフォルトの値を設定する.

        Parameters
        ----------
        browser: webdriver
            スクレイピングするためのwebdriverオブジェクト
        """
        browser.get('https://qiita.com')
        self.encoding = 'utf8mb4'
        self.html = browser.page_source.encode(self.encoding)

    def get_tag_ranking(self) -> dict:
        """
        Qiitaからタグランキングに関する情報を取得する関数.

        Returns
        -------
        tag_ranking_data: dict
            タグランキングを収めた辞書オブジェクト.
        """
        soup = BeautifulSoup(self.html, "html.parser")
        ra_tag_names = soup.find_all(class_='ra-Tag_name pr-1')
        tag_ranking_data = {}
        for i, ra_tag_name in enumerate(ra_tag_names):
            tag_ranking_data[i+1] = [ra_tag_name.text, 
            'https://qiita.com/tags/%s'%(ra_tag_name.text.lower())]
        return tag_ranking_data

    def get_tag_ranking_article(self, browser: webdriver, tag_ranking_data: dict):
        """
        各タグランキングに応じたトレンド記事のURLを取得する関数.
        """
        pass

if __name__ == "__main__":
    """
    main文. browserはhtmlの取得が終わり次第閉じること.エラーが出てきたときも同様.
    """
    try:
        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)
        print("start scrape")
        qgr = QiitaGetRanking(browser)
        ranking_data = qgr.get_tag_ranking()
        # qgr.get_tag_ranking_article(browser, ranking_data)
        print("connect to mysql")
        cm = connect_mysql.ConnectMySQL()
        cm.register_tag_ranking(ranking_data)
        print("done")
    except:
        browser.close()
        browser.quit()
    finally:
        browser.close()
        browser.quit()