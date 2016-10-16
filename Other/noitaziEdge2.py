import numpy as np
import cv2

if __name__ == '__main__':

    # 画像の読み込み
    img_src = cv2.imread("AA1.png", 1)

    # 2次微分による平準化
    img_tmp = cv2.Laplacian(img_src, cv2.CV_16S, 8)
    img_lap = cv2.convertScaleAbs(img_tmp)

    # 表示
    cv2.imshow("Show LAPLACIAN Image", img_lap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()