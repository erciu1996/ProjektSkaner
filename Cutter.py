import cv2
import numpy as np
from PIL import Image

class Cutter:
    def __init__(self):
        None

    def __call__(self, image, confin):
        self.image = image
        self.confin = confin
        wskaznik = self.max(confin)

        if (wskaznik==0):
            self.przypadek_0()
        elif(wskaznik == 1):
            self.przypadek_1()
        elif (wskaznik == 2):
            return self.przypadek_2()
        elif(wskaznik == 3):
            return self.przypadek_3()
        else:
            print("Nieznany przypadek")

    def max(self, confin):
        lista = []
        for i in range(4):
            lista.append(confin.screenCnt[i][0][0]+confin.screenCnt[i][0][1])
        wskaznik = lista.index(max(lista))
        return wskaznik

    def przypadek_0(self):
        src_pts = np.array([self.confin.screenCnt[2][0], self.confin.screenCnt[1][0], self.confin.screenCnt[0][0],self.confin.screenCnt[3][0]], dtype=np.float32)
        dst_pts = np.array([[0, 0], [400, 0], [400, 292], [0, 292]], dtype=np.float32)
        M = cv2.getPerspectiveTransform(src_pts, dst_pts)
        warp = cv2.warpPerspective(self.image, M, (400, 292))
        return warp

    def przypadek_1(self):
        src_pts = np.array([self.confin.screenCnt[3][0], self.confin.screenCnt[2][0], self.confin.screenCnt[1][0],self.confin.screenCnt[0][0]], dtype=np.float32)
        dst_pts = np.array([[0, 0], [400, 0], [400, 292], [0, 292]], dtype=np.float32)
        M = cv2.getPerspectiveTransform(src_pts, dst_pts)
        warp = cv2.warpPerspective(self.image, M, (400, 292))
        return warp

    def przypadek_2(self):
        src_pts = np.array([self.confin.screenCnt[0][0], self.confin.screenCnt[3][0], self.confin.screenCnt[2][0], self.confin.screenCnt[1][0]], dtype=np.float32)
        dst_pts = np.array([[0, 0], [400, 0], [400, 292], [0, 292]], dtype=np.float32)
        M = cv2.getPerspectiveTransform(src_pts, dst_pts)
        warp = cv2.warpPerspective(self.image, M, (400, 292))
        return warp

    def przypadek_3(self):
        src_pts = np.array([self.confin.screenCnt[1][0], self.confin.screenCnt[0][0], self.confin.screenCnt[3][0], self.confin.screenCnt[2][0]], dtype=np.float32)
        dst_pts = np.array([[0, 0], [400, 0], [400, 292], [0, 292]], dtype=np.float32)
        M = cv2.getPerspectiveTransform(src_pts, dst_pts)
        warp = cv2.warpPerspective(self.image, M, (400, 292))
        return warp