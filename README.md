# シスプロのWeb課題

## 入ってるもの

jetty, react, java, msql

## 使い方
docker-compose.ymlのファイルのあるディレクトリに入って, 

` docker-compose up -d --build `

これで起動.

` docker attach react_app ` もしくは, ` docker exec -it react_app /bin/ash ` でreact_appコンテナに接続.

接続後, lsコマンドで, qiita_frontがあれば, ` rm -rf qiita_front `を実行.

そのあと, ` npx create-react-app qiita_front ` を実行.

buildが始まるので終了後, lsコマンドでqiita_frontディレクトリがあることを確認後, control+P, Q(controlを押しながらPとQを順番に押す)を実行して, host環境に戻ること.

