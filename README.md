# Project Qtroid
シスプロのweb課題で作る予定のもの.

## 概要
本アプリケーションは,「Qtroid」と呼び,エンジニアリングに関する知識を記録・共有するためのサービスである「Qiita」内で,まず初めに閲覧者自身が気になる技術名(プログラミング言語や人工知能など)が書かれたタグを選択して, いいねと言う「Qiita」利用者がその記事につける評価が多い順に記事をソートし,その中にある参考文献(URL)をリストとしてまとめて,画面上に表示する.

## 入ってるもの
jetty, react, java, msql, python, selenium

## 使い方
docker-compose.ymlのファイルのあるディレクトリに入って, 

` docker-compose up -d --build `

これで起動.

### java
サーバーサイドで利用. servletを利用している.

### jetty
jettyサーバー. javaから利用.

### mysql
サーバーサイドでデータを保存して, フロントサイドで利用している.

### react
フロントサイドで利用. 

### python
サーバーサイドで利用. スクレイピングをするために利用.

### selenium
pythonで利用. jaascriptを利用しているサイトをスクレイピングをするのに必要.
