#!/usr/bin/env python

import cv2
import numpy as np


bild = cv2.imread('on.jpg')
# Bildausschnitt waehlen
cropped = bild[440:480, 680:720]
# cv2.imwrite("1.jpg",cropped)
# Untere Grenze
filter_from = np.array([200, 200, 200], np.uint8)
# Obere Grenze
filter_to = np.array([255, 255, 255], np.uint8)
# Filtere Bild
filtered = cv2.inRange(cropped, filter_from, filter_to)
# Zaehle anzahl von Bildpunkten, die nicht 0 (d.h. Schwarz) sind
amount = cv2.countNonZero(filtered)
print(amount)
