import cv2 as cv

img = cv.imread(r"img.jpg")

img_gray = cvtColor(img, COLOR_BGR2GRAY)
img_invert = bitwise_not(img_gray)
img_smoothing = GaussianBlur(img_invert, (41, 41),sigmaX=0, sigmaY=0)
sketch = img_division(img_gray, 255 - img_smoothing, scale=256)

cv.imshow("Frame", sketch)
