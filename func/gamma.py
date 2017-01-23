import os
import math
import json

global_path = os.path.realpath('../res/gamma')

def gamma_fun(pixel, gamma):
    return round(math.pow((pixel+0.5)/256, 1/gamma)*256 - 0.5)

def create_gamma_file(gamma):
    data = dict()
    for i in range(256):
        data[str(i)] = gamma_fun(i, gamma)
    with open(os.path.join(global_path, str(gamma)+'.json'), 'w') as f:
        json.dump(data, f)

gamma = 2.2
create_gamma_file(gamma)