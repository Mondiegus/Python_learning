import numpy as np
import cv2
import time
import mss
import pandas as pd
import keyboard
import os
import tensorflow as tf


def average_slope_intercept(frame, line_segments):
    """
    This function combines line segments into one or two lane lines
    If all line slopes are < 0: then we only have detected left lane
    If all line slopes are > 0: then we only have detected right lane
    """
    try:
        lane_lines = []
        height, width = frame.shape
        left_fit = []
        right_fit = []
        Ys = []
        cords = []
        ml = 0
        mr = 0
        boundary = 1 / 2
        left_region_boundary = width * (1 - boundary)  # left lane line segment should be on left 2/3 of the screen
        right_region_boundary = width * boundary  # right lane line segment should be on right 1/3 of the screen
        for line_segment in line_segments:
            for x1, y1, x2, y2 in line_segment:
                if x1 == x2:
                    continue
                Ys += [y1, y2]
                min_y = min(Ys)
                max_y = 700
                fit = np.polyfit((x1, x2), (y1, y2), 1)
                slope = fit[0]
                intercept = fit[1]
                if slope < 0:
                    if x1 < left_region_boundary and x2 < left_region_boundary:
                        left_fit.append((slope, intercept))
                else:
                    if x1 > right_region_boundary and x2 > right_region_boundary:
                        right_fit.append((slope, intercept))

        left_fit_average = np.average(left_fit, axis=0)
        if len(left_fit) > 0:
            x1 = (min_y - left_fit_average[1]) / left_fit_average[0]
            x2 = (max_y - left_fit_average[1]) / left_fit_average[0]
            cords.append([[int(x1), int(min_y), int(x2), int(max_y)]])
            ml = 1
        else:
            ml = 0

        right_fit_average = np.average(right_fit, axis=0)
        if len(right_fit) > 0:
            x1 = (min_y - right_fit_average[1]) / right_fit_average[0]
            x2 = (max_y - right_fit_average[1]) / right_fit_average[0]
            cords.append([[int(x1), int(min_y), int(x2), int(max_y)]])
            mr = 1
        else:
            mr = 0

        # print(ml, mr)
        return cords, ml, mr
    except:
        return 0, 0, 0


def draw_lines(img, lines):
    try:
        for line in lines:
            points = line[0]
            cv2.line(img, (points[0], points[1]), (points[2], points[3]), [0, 255, 0], 3)
    except:
        pass


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

model = tf.keras.models.load_model(r"C:\Users\Mondi\PycharmProjects\AI_Car\mymodel.h5")

with mss.mss() as sct:
    # Part of the screen to capture
    # monitor = {"top": 30, "left": -1920, "width": 640, "height": 480}
    monitor = {"top": 30, "left": 0, "width": 640, "height": 480}

    while "Screen capturing":
        last_time = time.time()

        img = np.array(sct.grab(monitor))
        img_resized = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (48, 64))
        img_resized = np.expand_dims(img_resized, axis=0)
        data = model.predict(img_resized)
        print(data)
        m1 = data[0]
        m2 = data[0]
        m12 = data[0]
        if m12 == 1:
            keyboard.press('W')
            time.sleep(0.08)
            keyboard.release('W')
            time.sleep(0.16)
            keyboard.release('d')
            keyboard.release('A')
            output_data = [0, 1, 0]

        if m2 == 1:
            # keyboard.release('W')
            keyboard.release('d')
            keyboard.press('A')
            output_data = [1, 0, 0]

        if m1 == 1:
            # keyboard.release('W')
            keyboard.release('A')
            keyboard.press('d')
            output_data = [0, 0, 1]

        if m1 == 0 and m2 == 0:
            # keyboard.release('W')
            keyboard.release('d')
            keyboard.release('A')
            output_data = [0, 0, 0]
            pass

        # Display the picture in HSV
        # cv2.imshow('OpenCV/Numpy grayscale1', mask)
        # cv2.imshow('OpenCV/Numpy grayscale2', processed_img)
        cv2.imshow('OpenCV/Numpy grayscale3', img)
        # cv2.imshow('OpenCV/Numpy grayscale4', cropped_edges2)

        # print("time: {}".format(time.time() - last_time))
        # print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
