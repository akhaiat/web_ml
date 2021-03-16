# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
#さっき作ったprediction.pyをimportする
import prediction

app = Flask(__name__)


@app.route('/')
def index():
    #最初はindex.htmlをそのまま返す
    return render_template("index.html")

#action="/send"を持ったformが送られたときにこの関数を呼び出す
@app.route('/send', methods=["GET", "POST"])
def send():

    #index.htmlのformから送られてきた画像データ(inputImage)を受け取る
    stream = request.files["inputImage"].stream
    im = Image.open(stream)

    #prediction.pyからprediction関数を呼び出して使う
    output = prediction.prediction(im)

    #結果をindex.html内のoutputの部分に埋め込んでhtmlを返す
    return render_template('index.html',output=output)

if __name__ == "__main__":
    app.debug=True
    app.run(host='localhost',port=5000)
