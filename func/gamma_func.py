import os
import math
import json

global_path = os.path.realpath('res/gamma')
global_tmp_data = dict()

def gamma_fun(pixel, gamma):
    return round(math.pow((pixel+0.5)/256, 1/gamma)*256 - 0.5)

def gamma_file_name(gamma):
    return os.path.join(global_path, str(gamma)+'.json')

def create_gamma_file(gamma):
    data = dict()
    for i in range(256):
        data[str(i)] = gamma_fun(i, gamma)
    with open(gamma_file_name(gamma), 'w') as f:
        json.dump(data, f)

def read_gamma_file(gamma):
    data = global_tmp_data.get(str(gamma))
    if data is None:
        data = json.load(open(gamma_file_name(gamma)))
        global_tmp_data[str(gamma)] = data
    return data


# export functions
def transform(pixel, gamma):
    if not os.path.exists(gamma_file_name(gamma)):
        create_gamma_file(gamma)
    data = read_gamma_file(gamma)
    return data[str(pixel)]

# 在Gamma校正之前，要先灰度化，否则报错
def tranform_image(im, gamma):
    px = im.load()
    i,j = 0,0
    while i<im.size[0]:
        while j<im.size[1]:
            px[i, j] = transform(px[i, j], gamma)
            j = j + 1
        i = i + 1


# gamma = 2.2
# create_gamma_file(gamma)
