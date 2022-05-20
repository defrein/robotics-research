import cv2
import imutils

image = cv2.imread('data\\es-profile.jpg')
cv2.imshow('Gambar Asli', image)

# TRANSLATION
X, Y = 150, 50
shifted = imutils.translate(image, X, Y)
# cv2.imshow("Shifted", shifted)
# cv2.waitKey(0)

# ROTATION
angle = 90
rotated = imutils.rotate(image, angle)
# cv2.imshow("Rotated", rotated)
# cv2.waitKey(0)

# RESIZE
# methods = [
#     ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
#     ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
#     ("cv2.INTER_AREA", cv2.INTER_AREA),
#     ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
#     ("cv2.INTER_LACZOS4", cv2.INTER_LACZOS4),
# ]

height, width = 300, 700
resize_cv = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
resize_im = imutils.resize(image, width=width)
# cv2.imshow("Resized CV", resize_cv)
# cv2.imshow("Resized IM", resize_im)
# cv2.waitKey(0)

# FLIP
flip_hor = cv2.flip(image, 1)
flip_ver = cv2.flip(image, 0)
flip_verhor = cv2.flip(image, -1)
# cv2.imshow("flip_hor", flip_hor)
# cv2.imshow("flip_ver", flip_ver)
# cv2.imshow("flip_verhor", flip_verhor)
# cv2.waitKey(0)

# CROPPING
bunga = image[48:225, 90:376]
wajah = image[227:384, 80:376]
cv2.imshow("Bunga", bunga)
cv2.imshow("Wajah", wajah)
cv2.waitKey(0)
