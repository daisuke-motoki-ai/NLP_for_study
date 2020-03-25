FROM nlp_for_k8s_python
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>

#  ref https://github.com/pollenjp/shell_script_for_setup/blob/30daf8f14e7e71b60af0a9fa04c3771121d6f93c/python-setup/pyenv-default-python3.5.2/pyenv-default-python3.5.2-install_jupyter-extensions.sh
#####------------------------------
#####  Jupyter Extensions
#####------------------------------

# 以下はbasebotebookの方にうつす
USER root
RUN apt-get update && apt-get install -yq --no-install-recommends \
    git

USER $NB_USER
ENTRYPOINT ["tini", "--"]

RUN yes | pip install --upgrade pip
RUN yes | pip install --quiet --no-cache-dir \
      jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable python-markdown/main  # MarkdownセルでPythonの変数を表示可能
RUN jupyter nbextension enable toc2/main             # TableOfContents

# 以下はbasebotebookの方にうつす
# 以下全て画像出力で必要だったもの
USER root
RUN apt install poppler-utils
RUN apt install poppler-data

# RUN pip install pdfplumber
RUN pip install Pillow
RUN pip install wheel
RUN pip install pdf2image
RUN pip install pdfminer
RUN pip install pdfplumber

RUN apt install xz-utils


# NLP 表記揺れ対策（正規化）
RUN pip install neologdn==0.4

# PyTorch 
RUN pip install torch==1.4.0

# pdf perser (camelot)
# https://camelot-py.readthedocs.io/en/master/user/install.html#install
RUN pip install camelot-py[cv] 