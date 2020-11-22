#Enes Karacabay

import cv2
import numpy as np

def read():  ### fotoyu açıp pixel listesini return ediyorum
    path = input("Fotoğrafın erişim adını giriniz(örn:'C:/Users/foto.jpg') : ")
    img = cv2.imread(path)
    return img

def circle(img):  ##fotodaki yuvarlak var mı diye arayan en kıymetli fonksiyonum...
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.5, 140, param1=100, param2=50, minRadius=70, maxRadius=500)
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 6)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 6)
    cv2.imwrite("detected_circle.jpg", img)
    print("Fotoğraftaki yuvarlak nesne bulundu ve 'detected_circle.jpg' olarak kaydedildi. ")


img = read()
circle(img)
