# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hz7BvIrE0AzXaTNbFFHTMvAeWKuJyweF
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("download.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)