import numpy as np
import cv2

# 2次微分による平準化
def laplacian(img):
    # 画像の読み込み
    img_src = cv2.imread(img, 1)
    # 2次微分による平準化
    img_tmp = cv2.Laplacian(img_src, cv2.CV_16S, 8)
    img_lap = cv2.convertScaleAbs(img_tmp)

    cv2.imshow("Show LAPLACIAN Image", img_lap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def hsv(img):
    # 画像の読み込み
    img_src = cv2.imread(img, 1)

    # RGBからHSVに変換
    img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

    # 表示
    cv2.imshow("Show HSV Image", img_hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def gray(img):
    # 画像の読み込み
    img_src = cv2.imread(img, 1)

    # RGBからグレースケールに変換
    img_gry = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

    # 表示
    cv2.imshow("Show LOW CONTRAST Image", img_gry)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':

    gray("AA10.png")
    laplacian("AA1.png")


