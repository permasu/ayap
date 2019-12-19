import sys
import numpy as np
import cv2 as cv
import math

hsv_min = np.array((120,140,4), np.uint8)
hsv_max = np.array((160, 140, 200), np.uint8)
color_yellow = (0,0,0)
if __name__ == '__main__':
    fn = 'kovi4m2.jpg'  # имя файла, который будем анализировать
    img = cv.imread(fn)
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours0, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours0:
        rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        center = (int(rect[0][0]), int(rect[0][1]))
        area = int(rect[1][0] * rect[1][1])  # вычисление площади
        if (area > 10000) & (area <100000):
            cv.drawContours(img, [box], 0, (255, 0, 0), 2)
            cv.circle(img, center, 5, color_yellow, 2)
            # вычисление координат двух векторов, являющихся сторонам прямоугольника
            edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
            edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

            # выясняем какой вектор больше
            usedEdge = edge1
            if cv.norm(edge2) > cv.norm(edge1):
                usedEdge = edge2
            reference = (1, 0)
            angle = 180.0 / math.pi * math.asin(
                (reference[0] * usedEdge[0] + reference[1] * usedEdge[1]) / (cv.norm(reference) * cv.norm(usedEdge)))
            LengthLongEdge = max(usedEdge[0],usedEdge[1]) -  min(usedEdge[0],usedEdge[1])
            normLength = LengthLongEdge/math.cos(angle)
            naturalLength = 427
            k=normLength/naturalLength
            z = round(1 / k,3)
            cv.putText(img, str(int(center[0])) + "," +str(int(center[1]))+"," +str(z),
                       (center[0] - 50, center[1] - 70), cv.FONT_HERSHEY_SIMPLEX, 0.7, color_yellow, 2)
    cv.imshow('contours', img)  # вывод обработанного кадра в окно
    cv.waitKey()
    cv.destroyAllWindows()