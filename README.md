# Project Qtroid
シスプロのweb課題で作る予定のもの.

## 概要
本アプリケーションは,「Qtroid」と呼び,エンジニアリングに関する知識を記録・共有するためのサービスである「Qiita」内で,まず初めに閲覧者自身が気になる技術名(プログラミング言語や人工知能など)が書かれたタグを選択して, いいねと言う「Qiita」利用者がその記事につける評価が多い順に記事をソートし,その中にある参考文献(URL)をリストとしてまとめて,画面上に表示する.

## 入ってるもの
jetty, react, java, msql, python, selenium

## 予定

pythonでスクレイピング, jsonの作成, mysqlへの登録をして, javaからその情報を取ってくる仕様

## 進捗

- [x] javaからmysqlへの接続
- [x] pythonからmysqlへの接続
- [x] javaからpythonの呼び出し
- [x] pythonでqiitaのスクレイピング
- [ ] フロント側との連携テスト
