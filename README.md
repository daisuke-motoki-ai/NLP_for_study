# Jupyter上でNLPを利用するための仮想環境
## Docker-composeを用いた仮想環境の立ち上げと終了
jupyter-Jij/middleware ディレクトリから以下のコマンドで立ち上げ

```sh
docker-compose -f docker-compose.yml down && docker-compose -f docker-compose.yml up -d --build && docker-compose exec science bash
```

以下のコマンドをブラウザ上のURLに書き込む

```sh
http://localhost:8285/
```


コンテナ内部に入っているので、Ctrl + D でexit すればjupyterアプリケーションは終了する。

## モジュールのインストール

Jupyter-Jij/middleware/jupyter_science/Dockerfile のコメントアウトの所を適宜変更して、必要なモジュールをインストール。
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

