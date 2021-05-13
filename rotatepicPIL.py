from PIL import Image
import time

image = Image.open('image.jpg')

start_time = time.time()
rotated = image.rotate(-90)

# image.show()

rotatedImage = rotated.save('rotated.jpg')
end_time = time.time()

print(f"this process took {start_time - end_time} seconds")