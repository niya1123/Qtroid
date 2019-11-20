import mysql.connector

class ConnectMySQL():
    """
    MySQLに接続して, 操作するクラス.
    """

    def __init__(self):
        """
        MySQLに接続するために必要ものの初期設定.
        """
        self.conn = mysql.connector.connect(
            user='user', 
            password='userpass', 
            host='mysql', 
            database='qiita_rank',
            charset='utf8')
        self.cur = self.conn.cursor()

    def register_tag_ranking(self, tag_ranking_data: dict):
        """
        MySQLのtag_rankingテーブルに値を入れる為の関数.
        """
        self.cur.execute("DROP TABLE IF EXISTS tag_ranking")

        self.cur.execute("CREATE TABLE tag_ranking (ranking int NOT NULL, tag_name VARCHAR(50) NOT NULL, tag_url VARCHAR(100) NOT NULL)")

        for rank in list(tag_ranking_data.keys()):
            self.cur.execute("INSERT INTO tag_ranking (ranking, tag_name, tag_url) VALUES (%d, '%s', '%s')"%(rank, tag_ranking_data[rank][0], tag_ranking_data[rank][1]))


    def register_trend_data(self, trend_data: dict):
        """
        MySQLにトレンドデータを登録する関数.
        """
        print('drop table')
        self.cur.execute("DROP TABLE IF EXISTS trend_data")

        print('create table')
        self.cur.execute("CREATE TABLE trend_data (ranking int NOT NULL, " 
                                                  "tag_name VARCHAR(50) NOT NULL, " 
                                                  "trend_title VARCHAR(255) NOT NULL, " 
                                                  "like_count int NOT NULL, " 
                                                  "trend_url VARCHAR(100) NOT NULL)")

        print('insert table')
        for i, tag_name in enumerate(list(trend_data.keys())):
            for trend_article_data in list(trend_data[tag_name]):
                self.cur.execute("INSERT INTO trend_data (ranking, tag_name, trend_title, like_count, trend_url) VALUES (%d, '%s', '%s', %d, '%s')"%
                ( list(trend_article_data.keys())[0], 
                tag_name, 
                trend_article_data.get( list(trend_article_data.keys())[0] )[0],
                trend_article_data.get( list(trend_article_data.keys())[0] )[1], 
                trend_article_data.get( list(trend_article_data.keys())[0] )[2] )
                )

    def connection_closed(self):
        self.conn.commit()
        print('save')
        self.conn.close()
        print("closed")