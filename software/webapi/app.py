# -*- coding: utf-8 -*-
# https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import MeCab

app = Flask(__name__)

# Main
def picked_up():
    messages = [
        "何かコメントしてみてください",
        "AIボットです。コメントをどうぞ",
    ]
    return np.random.choice(messages)

def tokenize(text):
    tagger = MeCab.Tagger()
    node = tagger.parseToNode(text)
    tokens = []
    while node:
        if node.surface != '':
            tokens.append(node.surface)
        node = node.next
    return tokens
from os.path import dirname, join, normpath

import MeCab
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


class DialogueAgent:
    def __init__(self):
        self.tagger = MeCab.Tagger()

    def _tokenize(self, text): # 形態素解析
        node = self.tagger.parseToNode(text)

        tokens = []
        while node:
            if node.surface != '':
                tokens.append(node.surface)
 
            node = node.next
        return tokens

    def train(self, texts, labels): # 2. 文章とラベルからニューラルネットワークを更新
        pipeline = Pipeline([
            ('vecttorizer', CountVectorizer(tokenizer=self._tokenize)), 
            ('classifier', SVC()),
        ])
        pipeline.fit(texts, labels)
        self.pipeline = pipeline

    def predict(self, texts): # 3. 他の文章でのニューロンの反応をチェック
        return self.pipeline.predict(texts)

# Routing
@app.route('/')
def index():
    title = ""
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['POST', 'GET'])
def post():


    title = ""
    if request.method == 'POST':

        BASE_DIR = normpath(dirname('__file__'))

        training_data = pd.read_csv(join(BASE_DIR, './training_data.csv'))  # 学習用読み込み文章

        dialogue_agent = DialogueAgent()
        dialogue_agent.train(training_data['text'], training_data['label']) # 学習用読み込み文章とラベルの組を学習

        with open(join(BASE_DIR, './replies.csv')) as f:  # 応答文章
            replies = f.read().split('\n')
        # input_text = input()
        input_text = request.form['name']
        predictions = dialogue_agent.predict([input_text])
        predicted_class_id = predictions[0]





        words = replies[predicted_class_id]
        return render_template('index.html',
                               name=words, title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
