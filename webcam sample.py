# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:48:56 2020

@author: KOWSHIKI
"""


import cv2

v=cv2.VideoCapture(0)

while(True):
    r,f=v.read()
    if r==True:
        cv2.imshow("output",f)
        if cv2.waitKey(0) & 0xFF=='q':
            break
    else:
        break
cv2.release()
cv2.destroyAllWindows()

