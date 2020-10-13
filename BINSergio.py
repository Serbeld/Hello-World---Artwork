# -*- coding: utf-8 -*-

import cv2

img = cv2.imread('Hellooo.jpg',2)

img = cv2.resize(img, (1920, 1080), interpolation=cv2.INTER_LANCZOS4)

ret, th1 = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)

#cv2.INTER_NEAREST cv2.INTER_LANCZOS4

cv2.imwrite('HelloWorld_HD.png', th1)