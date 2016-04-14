#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

import picamera
import picamera.array
import cv2
import numpy
import time

RESOLUTION = (1920, 1080)
CUTOUT = ((187, 187 + 15), (693, 693 + 15))
AMOUNT = (CUTOUT[0][1] - CUTOUT[0][0]) * (CUTOUT[1][1] - CUTOUT[1][0])
THRESHOLD_PIXELS = 0.4 
THRESHOLD_FRAMES = 10
THRESHOLD_FRAMES_ON = 3

LIGHT_OFF = numpy.array([180, 30, 30], numpy.uint8)
LIGHT_ON = numpy.array([255, 255, 255], numpy.uint8)


assert AMOUNT >= THRESHOLD_PIXELS
assert THRESHOLD_FRAMES > THRESHOLD_FRAMES_ON


def camera_frames():
    camera = picamera.PiCamera()
    time.sleep(0.2)
    camera.resolution = RESOLUTION
    raw_capture = picamera.array.PiRGBArray(camera, size=RESOLUTION)
    time.sleep(0.2)
    frame = camera.capture(raw_capture, format="bgr",
                                               use_video_port=True)
    camera.close()
    return raw_capture


def cut_out_frames():
    frame = camera_frames()
    return frame.array[CUTOUT[0][0]:CUTOUT[0][1], CUTOUT[1][0]:CUTOUT[1][1]]


def bright_pixels():
    frame = cut_out_frames()
    filtered = cv2.inRange(frame, LIGHT_OFF, LIGHT_ON)
    return cv2.countNonZero(filtered) 

def bright_pixels_relative():
    bright_pixels_amount = bright_pixels()
    return bright_pixels_amount / AMOUNT


def stove_is_on():
     bright_pixels_amount = bright_pixels()
     print(bright_pixels_amount)
     return bright_pixels_amount >= THRESHOLD_PIXELS

def stove_is_on_filtered():
    last_results = [False * THRESHOLD_FRAMES]
    for stove_is_on_state in stove_is_on():
        last_results.pop()
        last_results.append(stove_is_on_state)
        yield sum(last_results) >= THRESHOLD_FRAMES_ON


if __name__ == "__main__":
    stove_is_on_state = stove_is_on()
    if stove_is_on_state:
         print("ON!")
    else:
         print("OFF")
