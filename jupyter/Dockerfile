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