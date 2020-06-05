import numpy as np
import cv2

cap = cv2.VideoCapture(0)

t0 = cap.read()[1]
t1 = cap.read()[1]

# 將此兩張影像分別進行灰階及高斯模糊處理
gray1 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)

blur1 = cv2.GaussianBlur(gray1,(7,7),0)
blur2 = cv2.GaussianBlur(gray2,(5,5),0)

# 使用cv2.absdiff計算並得出兩張影像的差異圖形
d = cv2.absdiff(blur1, blur2)

# 將差異圖形進行二值化處理(即黑白化)
ret, th = cv2.threshold( d, 10, 255, cv2.THRESH_BINARY )

# 使用cv2.dilate進行擴張處理，可避免當移動速度過快差異不顯著時加強
dilated=cv2.dilate(th, None, iterations=1)

contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

areas = [cv2.contourArea(c) for c in contours]

max_index = np.argmax(areas)

cnt=contours[max_index]

x,y,w,h = cv2.boundingRect(cnt)

cv2.drawContours(layer, cnt, -1, markColor, 2)

cv2.rectangle(layer,(x,y),(x+w,y+h), markColor,2)

Cutted = t0[y:y + h, x:x + w]

layer = layer[y:y + h, x:x + w]
