# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image, ImageEnhance, ImageOps
from keras.models import model_from_json
import tensorflow as tf

def prediction(im):
    # モデルの読み込み
    model = model_from_json(open('mnist_mlp_model.json', 'r').read())
    # 学習結果の読み込み
    model.load_weights('mnist_mlp_weights.h5')

    #画像を明瞭化する
    im_enh = ImageEnhance.Brightness(im).enhance(2)
    #画像をグレースケール化する
    im_gray = im_enh.convert(mode="L")
    #画像を28x28にリサイズする
    im_8x8 = im_gray.resize((28,28))
    im_inv = ImageOps.invert(im_8x8)
    #2次元のndarrayに変更
    x_im2d = np.asarray(im_inv)
    x_mult = x_im2d/255
    x_mult = x_mult.reshape(1,28,28,1)

    output = model.predict_classes(x_mult,batch_size=1)[0]
    return output
