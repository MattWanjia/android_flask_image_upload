from scipy import ndimage
import imageio
import matplotlib.pyplot as plt
import time

start_time = time.time()
image = imageio.imread('image.jpg')
#rotation angle in degree
rotated = ndimage.rotate(image, -90)
rotatedImage = imageio.imwrite(rotated, 'rotated2.jpg')
end_time = time.time()

print(f"this process took {start_time - end_time} seconds")

