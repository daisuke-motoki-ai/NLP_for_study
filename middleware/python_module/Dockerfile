FROM jupyter/minimal-notebook
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>

#####------------------------------
#####  Install python module of NLP
#####------------------------------
RUN yes | pip install --upgrade pip
RUN yes | pip install --quiet --no-cache-dir \
    pandas \
    matplotlib \
    flask \
    mecab-python3 \
    sklearn \
    gensim \