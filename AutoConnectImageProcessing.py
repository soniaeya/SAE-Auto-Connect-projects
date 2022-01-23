import skimage.io
import skimage.color
from matplotlib import pyplot as plt


img = skimage.io.imread(fname="nyankat.jpeg")   #read original image

skimage.io.imshow(img)
plt.show()  #Shows original image

gray_img = skimage.color.rgb2gray(img)
skimage.io.imshow(gray_img)
plt.show() #Shows greyscale image

from skimage.transform import rotate
rotated_img = rotate(gray_img, 90.0)

skimage.io.imshow(rotated_img)
plt.show()  #Shows rotated 90 degrees image