from medpy.io import load
from deepbrain import Extractor
from PIL import Image, ImageDraw
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import scipy
import scipy.misc
import sys
import os


def gif_converter(path):
    print("here is the path" + path)
    rawimg, image_header = load(path)
    t = rawimg
    ws = []
    for i in range(193):
        scipy.misc.imsave('static/pics/'+str(i) +
                          'ws'+'.jpg', rawimg[:, :, i])
    for o in range(193):
        ws.append(Image.open('static/pics/' +
                             str(o)+'ws'+'.jpg').convert('P'))

    ws[0].save('static/gify/withskull.gif', save_all=True,
               append_images=ws[1:], optimize=True, duration=50, loop=0)

    for j in range(193):
        os.remove('static/pics/'+str(j) + 'ws' + '.jpg')


def main():
    path = 'static/uploads1/00000.mnc'
    print(path)

    gif_converter(path)
    print("Working done")


if __name__ == "__main__":
    main()
