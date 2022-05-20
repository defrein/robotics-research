
import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype='uint8')

# b, g, r
hijau = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), hijau)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# b, g, r
merah = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), merah, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#b, g, r
biru = (255, 0, 0)
cv2.rectangle(canvas, (10, 10), (60, 60), biru)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), merah)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (200, 50), (225, 125), hijau, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# menggambar lingkaran
# reset canvas
canvas = np.zeros((300, 300, 3), dtype='uint8')
centeX, centerY = canvas.shape[1] // 2, canvas.shape[0] // 2
putih = (255, 255, 255)

# cv2.circle(canvas, (centeX, centerY), 15, putih)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# rectangle loop
for r in range(0, 175, 25):
    cv2.circle(canvas, (centeX, centerY), r, putih)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# menggambar abstrak
# reset canvas
canvas = np.zeros((300, 300, 3), dtype='uint8')

for i in range(0, 25):
    r = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,)).tolist()

    cv2.circle(canvas, tuple(pt), r, color, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.imwrite('output3.jpg', canvas)

# menggambar rectangle di gambar rimuru
canvas = cv2.imread('data\\rimuru.jpg')
cv2.rectangle(canvas, (100, 100), (600, 500), merah)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.imwrite('output-rimuru3.jpg', canvas)
