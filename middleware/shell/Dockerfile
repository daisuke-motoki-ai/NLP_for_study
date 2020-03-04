FROM middleware_python_module
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>
#####------------------------------
#####  shell & editor environment 
#####------------------------------
# ホームディレクトリ
WORKDIR $HOME
USER root

RUN apt-get update && apt-get install -yq --no-install-recommends \
      tmux \
      vim
#####------------------------------
#####  zsh setting 
#####------------------------------
RUN apt upgrade -y
RUN apt install -y zsh powerline fonts-powerline
RUN chsh -s /bin/zsh
# oh-my-zsh
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
RUN cp $HOME/.oh-my-zsh/templates/zshrc.zsh-template $HOME/.zshrc

#####------------------------------
#####  peco 
#####------------------------------

# tarファイルをダウンロード
RUN wget "https://github.com/peco/peco/releases/download/v0.5.1/peco_linux_386.tar.gz"

# 解凍
RUN tar xzvf peco_linux_386.tar.gz
RUN rm peco_linux_386.tar.gz

WORKDIR $HOME/peco_linux_386
# 実行権限変更
RUN chmod +x peco
# PATHの通っている所にpecoを配置
RUN cp peco /usr/local/bin

#####------------------------------
#####  python 
#####------------------------------

RUN pip install autopep8
RUN pip install flake8