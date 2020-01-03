import numpy as np
import cv2
import time
import mss
import numpy
import keyboard

def make_points(frame, line):
    height, width = frame.shape
    slope, intercept = line
    y1 = height  # bottom of the frame
    y2 = int(y1 * 1 / 2)  # make points from middle of the frame down

    # bound the coordinates within the frame
    x1 = max(-width, min(2 * width, int((y1 - intercept) / slope)))
    x2 = max(-width, min(2 * width, int((y2 - intercept) / slope)))
    return [[x1, y1, x2, y2]]

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
        boundary = 1/2
        left_region_boundary = width * (1 - boundary)  # left lane line segment should be on left 2/3 of the screen
        right_region_boundary = width * boundary # right lane line segment should be on right 1/3 of the screen
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
        return 0,0, 0

def draw_lines(img, lines):
    try:
        for line in lines:
            points = line[0]
            cv2.line(img,(points[0], points[1]), (points[2], points[3]), [0,255,0], 3)
    except:
        pass
    
def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked
    
def process_img(original_image):

    #saturated = Binarize[ColorConvert[original_image, "Grayscale"], .9]


    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    #processed_img = cv2.equalizeHist(processed_img)
    #processed_img = cv2.bilateralFilter(processed_img, 5, 50, 50)
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
    processed_img = cv2.Canny(processed_img, threshold1 = 50, threshold2 = 150)
    vertices = np.array([[10,700],[40,300],[140,300], [560,300],[630,300],[860,300],[960,300],[1000,700]])
    cropped_edges = roi(processed_img, [vertices])
    line_segments = cv2.HoughLinesP(cropped_edges,1, np.pi/180, 10, np.array([]), 40, 20)
    lane_lines = average_slope_intercept(processed_img, line_segments)
    #print(lane_lines)
    draw_lines(original_image, line_segments)
    return processed_img

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 30, "left": -1920, "width": 640, "height": 480}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        #cv2.imshow("OpenCV/Numpy normal", img)

        # Convert the picture to HSV
        img_HSV  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Get lines color
        mask_yellow = cv2.inRange(img_HSV, (27, 80, 130), (30, 175, 255))
        mask_black = cv2.inRange(img_HSV, (0, 0, 0), (180, 255, 1))
        mask_brown = cv2.inRange(img_HSV, (10, 40, 150), (20, 88, 230))


        mask = cv2.bitwise_or(mask_yellow, mask_black)
        mask = cv2.bitwise_or(mask, mask_brown)
        # mask = cv2.bitwise_and(img, img, mask=mask)

        # vertices = np.array([[160, 250], [250, 200], [370, 200], [480, 250]])
        vertices = np.array([[160, 350], [160, 280], [280, 200], [360, 200], [480, 280], [480, 350], [410, 350], [350, 250], [270, 250], [230, 350]])

        cropped_edges = roi(mask, [vertices])
        cropped_edges2 = roi(img, [vertices])
        processed_img = cv2.GaussianBlur(cropped_edges, (5, 5), 0)
        processed_img = cv2.Canny(processed_img, threshold1=150, threshold2=200)
        line_segments = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 10, np.array([]), minLineLength=9, maxLineGap=1)
        lane_lines, m1, m2 = average_slope_intercept(processed_img, line_segments)
        print(m1, m2)
        draw_lines(img, lane_lines)

        if m1 == 1 and m2 == 1:
            # keyboard.press('W')
            keyboard.release('d')
            keyboard.release('A')
        if m1 == 0 and m2 == 1:
            # keyboard.release('W')
            keyboard.release('d')
            keyboard.press('A')
        if m1 == 1 and m2 == 0:
            # keyboard.release('W')
            keyboard.release('A')
            keyboard.press('d')
        if m1 == 0 and m2 == 0:
            # keyboard.release('W')
            keyboard.release('d')
            keyboard.release('A')
            pass

        # Display the picture in HSV
        cv2.imshow('OpenCV/Numpy grayscale1', mask)
        cv2.imshow('OpenCV/Numpy grayscale2', processed_img)
        cv2.imshow('OpenCV/Numpy grayscale3', img)
        cv2.imshow('OpenCV/Numpy grayscale4', cropped_edges2)

        print("time: {}".format(time.time() - last_time))
        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break










# while(True):
#     printscreen_pill = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0,100,640, 480))), cv2.COLOR_BGR2RGB)
#     processed_img2 = cv2.cvtColor(printscreen_pill, cv2.COLOR_BGR2GRAY)
#
#     new_screen = process_img(printscreen_pill)
#     cv2.imshow('window2', new_screen)
#
#
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
