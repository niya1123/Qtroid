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
        self.cur.execute("CREATE TABLE tag_ranking (id int NOT NULL, tag_name VARCHAR(50) NOT NULL, tag_url VARCHAR(100) NOT NULL)")
        print('insert table')
        for rank in list(tag_ranking_data.keys()):
            self.cur.execute("INSERT INTO tag_ranking (id, tag_name, tag_url) VALUES (%d, '%s', '%s')"%(rank, tag_ranking_data[rank][0], tag_ranking_data[rank][1]))


    def register_trend_data(self, trend_data: dict):
        """
        MySQLにトレンドデータを登録する関数.
        """
        print('drop table')
        self.cur.execute("DROP TABLE IF EXISTS trend_data")

        print('create table')
        self.cur.execute("""CREATE TABLE trend_data (
                                                id int NOT NULL,
                                                tag_name VARCHAR(100) NOT NULL,
                                                trend_title VARCHAR(255) NOT NULL,
                                                like_count int NOT NULL,
                                                trend_url VARCHAR(100) NOT NULL)""")

        print('insert table')
        # for tag_name in list(trend_data.keys()):
        #     for trend_article_data in list(trend_data[tag_name]):
        #         self.cur.execute("INSERT INTO trend_data (id, tag_name, trend_title, like_count, trend_url) VALUES (%d, '%s', '%s', %d, '%s')"% 
        #                         ( 
        #                         list(trend_article_data.keys())[0], 
        #                         tag_name, 
        #                         # trend_article_data.get( list(trend_article_data.keys())[0] )[0],
        #                         "hoge",
        #                         trend_article_data.get( list(trend_article_data.keys())[0] )[1], 
        #                         trend_article_data.get( list(trend_article_data.keys())[0] )[2]
        #                         )
        #         )
        query = 'INSERT INTO trend_data (id, tag_name, trend_title, like_count, trend_url) VALUES (%s, %s, %s, %s, %s)'
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
       

    def connection_closed(self):
        self.conn.commit()
        print('save')
        self.conn.close()
        print("closed")