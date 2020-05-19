import numpy as np
import cv2
# from matplotlib import pyplot as plt

# 使用 OpenCV 讀取圖檔
img_bgr = cv2.imread('pika.png')

# 將 BGR 圖片轉為 RGB 圖片
img_rgb = img_bgr[:,:,::-1]

# 旋轉圖片,預設逆時針90,(img_rgb,2)為180,(img_rgb,-1)為順時針90
# img90=np.rot90(img_rgb)

# #以灰階格式匯入
# img_gray = cv2.imread('pika.png', 0)

# #檢查匯入後numpy陣列類型，長寬格式
# print type(img), img.shape, img.dtype

#產生圖片窗口,第二參數可自由縮放大小
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.imshow("window", img_rgb)

# plt.imshow(img_rgb)
# plt.show()

#等待使用者指令,0為永遠等待
cv2.waitkey(0)

#關閉所有opengl視窗
cv2.destroyAllWindows()

# #輸出圖片,可照副檔名格式輸出
# cv2.imwrite('output.jpg', img_rgb)

