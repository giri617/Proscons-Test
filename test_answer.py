import cv2
import numpy as np

#画像の読み込み
im = cv2.imread("milkdrop.png")
img = im.copy()


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 136, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#最大の面積を持つ領域を特定
max_sq = 0
max_id = -1

for i in range(len(contours)):
    im_con = img.copy()
    if cv2.contourArea(contours[i]) > max_sq:
       max_id = i
       max_sq = cv2.contourArea(contours[i])



#edge = cv2.drawContours(img, contours, max_id, (0,255,0), 3)

mask = np.zeros_like(gray)
cv2.drawContours(mask, [contours[max_id]], -1, color=255, thickness=-1)


im[mask == 0] =[0,0,0]

cv2.imshow("im",im)

#cv2.imshow("thresh", thresh)
#cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('answer.jpg', im)
