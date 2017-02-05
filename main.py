import math
from PIL import Image

from func import gamma_func

# im = Image.open('img/a.jpg')

# # 灰度化
# im = im.convert(mode='L')
# # Gamma校正
# gamma_func.tranform_image(im, 2.2)

# im.save('out_img/a.jpg')


def calc_pixel(px, size, i, j):
    x = 1
    if i > 0 and i < size[0] - 1:
        x = px[i + 1, j] - px[i - 1, j]
    if x == 0:
        x = 1

    y = 1
    if j > 0 and j < size[1] - 1:
        y = px[i, j + 1] - px[i, j - 1]
    if y == 0:
        y = 1

    obj = dict()
    obj['x'] = x
    obj['y'] = y
    obj['grad'] = (x**2+y**2)**0.5
    obj['grad_direction'] = 1/math.tan(y/x)
    return obj

im = Image.open('out_img/a.jpg')

data = []

px = im.load()
for i in range(im.size[0]):
    data.append([])
    for j in range(im.size[1]):
        data[i].append(calc_pixel(px, im.size, i, j))


for i in range(im.size[0]):
    for j in range(im.size[1]):
        t1 = data[0][0]
        t2 = data[i][j]
        if t1['x'] != t2['x'] or t1['y'] != t2['y']:
            print(t1)
            print(t2)

