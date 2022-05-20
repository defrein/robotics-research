from email.mime import image
import cv2

image = cv2.imread('data\\rimuru.jpg')
(h, w) = image.shape[:2]

cv2.imshow('Gambar rimuru', image)

# informasi pixel
(b, g, r) = image[0, 0]
print("Piksel pada (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0, 0] = (255, 0, 0)
(b, g, r) = image[0, 0]
print("Piksel pada (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Membagi gambar jadi 4
(cX, cY) = (w//2, h//2)
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow('Top Left', tl)
cv2.imshow('Top right', tr)
cv2.imshow('Bottom Right', br)
cv2.imshow('Bottom Left', bl)

# Manipulasi gambar
image[0:cY, 0:cX] = (255, 255, 255)
cv2.imshow('Gambar rimuru manipulasi', image)

cv2.waitKey(0)
