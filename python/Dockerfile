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
    gensim
RUN yes | pip install --quiet --no-cache-dir \
    Cython
RUN yes | pip install --quiet --no-cache-dir \
    scikit-image 
RUN yes | pip install --quiet --no-cache-dir \
    imgaug \
    pycocotools \
    tensorflow==1.15 \
    keras==2.1.1
    # keras==2.2.5 \
    # tensorflow==1.15.0 \
    # opencv-python==3.4.5.20