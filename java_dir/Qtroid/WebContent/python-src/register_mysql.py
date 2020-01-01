import mysql.connector, emoji

class RegisterMySQL():
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
            charset='utf8mb4')
        self.cur = self.conn.cursor()

    def register_tag_ranking(self, tag_ranking_data: dict):
        """
        MySQLのtag_rankingテーブルに値を入れる為の関数.
        """
        print('drop table')
        self.cur.execute("DROP TABLE IF EXISTS tag_ranking")
        print('create table')
        self.cur.execute("CREATE TABLE tag_ranking (tag_id int NOT NULL, tag_name VARCHAR(50) NOT NULL, tag_url VARCHAR(100) NOT NULL)")
        print('insert table')
        for rank in list(tag_ranking_data.keys()):
            self.cur.execute("INSERT INTO tag_ranking (tag_id, tag_name, tag_url) VALUES (%d, '%s', '%s')"%(rank, tag_ranking_data[rank][0], tag_ranking_data[rank][1]))


    def get_tag_urls(self):
        """
        tag_rankingからtag_urlを取得する関数.
        """
        self.cur.execute("select tag_url from tag_ranking")

        rows = self.cur.fetchall()
        tag_urls = []
        for row in rows:
            tag_urls.append(row[0])
        return tag_urls

    def register_trend_data(self, trend_data: dict):
        """
        MySQLにトレンドデータを登録する関数.
        """
        print('drop table')
        self.cur.execute("DROP TABLE IF EXISTS trend_data")

        print('create table')
        self.cur.execute("""CREATE TABLE trend_data (
                                                tag_id int NOT NULL,
                                                tag_name VARCHAR(50) NOT NULL,
                                                trend_title VARCHAR(255) NOT NULL,
                                                like_count int NOT NULL,
                                                trend_url VARCHAR(100) NOT NULL)""")

        print('insert table')
        
        query = 'INSERT INTO trend_data (tag_id, tag_name, trend_title, like_count, trend_url) VALUES (%s, %s, %s, %s, %s)'
        for tag_name in list(trend_data.keys()):
            for trend_article_data in list(trend_data[tag_name]):
                self.cur.execute(
                    query,
                    (
                        list(trend_article_data.keys())[0], 
                        tag_name,
                        ''.join(['' if c in emoji.UNICODE_EMOJI else c for c in trend_article_data.get( list(trend_article_data.keys())[0] )[0]]),
                        trend_article_data.get( list(trend_article_data.keys())[0] )[1], 
                        trend_article_data.get( list(trend_article_data.keys())[0] )[2]
                    )
                )

    def get_trend_data(self):
        """
        trend_dataからtrend_urlを取得する関数.
        """
        self.cur.execute("select tag_name ,trend_title,trend_url from trend_data")

        rows = self.cur.fetchall()
        trend_data = []
        for row in rows:
            trend_data.append([row[0], row[1], row[2]])
        return trend_data


    def register_article_data(self, article_data: dict):
        """
        MySQLにトレンドデータを登録する関数.
        """
        print('drop table')
        self.cur.execute("DROP TABLE IF EXISTS article_data")

        print('create table')
        self.cur.execute("""CREATE TABLE article_data (
                                                tag_name VARCHAR(50) NOT NULL,
                                                trend_title VARCHAR(255) NOT NULL,
                                                link VARCHAR(255) NOT NULL)""")

        print('insert table')
        query = 'INSERT INTO article_data (tag_name, trend_title, link) VALUES (%s, %s)'
        for tag_name in (list(article_data.keys())):
            for data in (list(article_data[tag_name])):
                self.cur.execute(
                    query,
                    (
                        tag_name,
                        ''.join(['' if c in emoji.UNICODE_EMOJI else c for c in data[0]]),
                        data[1]
                    )
                )
         

    def connection_closed(self):
        self.conn.commit()
        print('save')
        self.conn.close()
        print("closed")