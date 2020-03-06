# Docker-composeを用いた仮想環境の立ち上げと終了

```sh
git clone https://github.com/daisuke-motoki-ai/NLP_for_study.git

cd NLP_for_study/middleware

docker-compose -f docker-compose.yml down && docker-compose -f docker-compose.yml up -d --build && docker-compose exec shell tmux
```

# jupyter環境へのアクセス

以下のコマンドをブラウザ上のURLに書き込む

http://localhost:8285/


# webフレームワークFlaskの実行

以下にアクセス

http://0.0.0.0:5000/ 


# 終了の仕方


shell コンテナ内部に入っているので、Ctrl + D でコンテナから出ることができる。

コンテナを終了する際は以下

```
docker-compose -f docker-compose.yml down
```


# モジュールのインストール

NLP_for_study/middleware/python_module/Dockerfile のコメントアウトの所を適宜変更して、必要なモジュールをインストール。
```sh
FROM jupyter/datascience-notebook
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>


RUN pip install --upgrade pip && pip install -U cmake 
RUN pip install openjij

# 必要なモジュールは以下のような形で連ねて書くこともできる
# RUN pip install \
#     geopandas \
#     descartes \
#     dwave_networkx

USER $NB_USER
ENTRYPOINT ["tini", "--"]
CMD ["jupyter", "notebook"]
```

