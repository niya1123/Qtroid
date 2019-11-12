# シスプロのWeb課題

## 入ってるもの

jetty, react, java, msql

## 使い方
docker-compose.ymlのファイルのあるディレクトリに入って, 

` docker-compose up -d --build `

これで起動.

次に, reactのコンテナに入る.

` docker attach react_app `

その後, ` npx create-react-app qiita_front ` を実行する.

qiita_frontというディレクトリが生成されていることを確認して, ` control+P, Q `(controlを押しながら, pとqを順番に押す)を実行する.