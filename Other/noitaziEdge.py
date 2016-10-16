import numpy as np
import cv2

if __name__ == '__main__':

    # 画像の読み込み
    gray = cv2.imread("AA10.png", 1)

    # 平均化する画素の周囲の大きさを指定する。
    # (5, 5) の場合、個々の画素の地点の周囲5×5マスの平均をとる。
    # 数値が大きいほどぼやける。
    average_square = (25, 25)

    # x軸方向の標準偏差
    sigma_x = 1

    # Gaussianオペレータを使用して平滑化
    img_gauss = cv2.GaussianBlur(gray, average_square, sigma_x)

    # エッジの抽出
    edge = cv2.Canny(img_gauss, 100, 200)

    img_keypoint = edge

    # キーポイントの検出
    gftt = cv2.FastFeatureDetector_create()
    keypoints = gftt.detect(edge)

    # キーポイントの数をターミナル上に表示
    print(len(keypoints))

    # 表示
    img_keypoint = cv2.drawKeypoints(edge, keypoints, img_keypoint)
    cv2.imshow("Show Image", img_keypoint)
    cv2.waitKey(0)
    cv2.destroyAllWindows()