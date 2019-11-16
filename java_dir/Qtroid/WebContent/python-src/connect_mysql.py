# mysqlへの接続お試し

import mysql.connector

conn = mysql.connector.connect(user='root', password='root', host='mysql', database='test')
cur = conn.cursor()

cur.execute("select * from user;")

for row in cur.fetchall():
    print(row[0],row[1])

cur.close
conn.close