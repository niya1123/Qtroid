# mysqlへの接続お試し

# import mysql.connector

# conn = mysql.connector.connect(user='root', password='root', host='mysql', database='test')
# cur = conn.cursor()

# cur.execute("select * from user;")

# for row in cur.fetchall():
#     print(row[0],row[1])

# cur.close
# conn.close

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

        self.cur.execute("CREATE TABLE tag_ranking (ranking int NOT NULL, tag_name VARCHAR(50) NOT NULL, url VARCHAR(500) NOT NULL)")

        for rank in list(tag_ranking_data.keys()):
            self.cur.execute("INSERT INTO tag_ranking (ranking, tag_name, url) VALUES (%d, '%s', '%s')"%(rank, tag_ranking_data[rank][0], tag_ranking_data[rank][1]))

        self.conn.commit()
        self.conn.close()
