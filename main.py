from PIL import Image

# im = Image.open('img/a.jpg')
# im.convert(mode='L').save('out_img/a.jpg')


im = Image.open('out_img/a.jpg')
px = im.load()

i,j = 0,0

# while i<im.size[0]:
#     while j<im.size[1]
#         pass

print(px[i, j])
print(px[im.size[0]-1, im.size[1]-1])
