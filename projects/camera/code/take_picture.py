#!/usr/bin/env python

import picamera
import picamera.array
import io
import time
import cv2
# import numpy as np

stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='bgr')
        image = stream.array
        im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("1.jpg", image)
        cv2.imwrite("2.jpg", im)
