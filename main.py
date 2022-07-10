# PACKAGESx
import cv2
import datetime
import numpy as np
from objTracker import *

# FLAG
ids_lst = []
spd_lst = []
end = 0

# TRACKER OBJ
tracker = EuclideanDistTracker()

# CAPTURE INPUT VIDEO STREAM
cap = cv2.VideoCapture("resources/traffic.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
frame_count = 0

# KERNALS
kernalOp = np.ones((3, 3), np.uint8)
kernalCl = np.ones((11, 11), np.uint8)
kernalEr = np.ones((5, 5), np.uint8)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)


while True:

    # OBJ DETECTION

    ret, frame = cap.read()

    if ret == True:
        frame_count += 1

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    height, width, _ = frame.shape

    # EXTRACT ROI
    roi = frame[50:540, 200:960]

    # MASKING

    fgmask = fgbg.apply(roi)
    ret, binImg = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    opening = cv2.morphologyEx(binImg, cv2.MORPH_OPEN, kernalOp)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernalCl)
    er_img = cv2.erode(closing, kernalEr)

    # CONTOURS & BOUNDING BOX
    contours, _ = cv2.findContours(er_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # THRESHOLD
        if area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 255, 0), 3)
            detections.append([x, y, w, h])

    # # OBJ TRACKING
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id

        if (tracker.getsp(id) < tracker.limit()):
            cv2.putText(roi, str(id) + " " + str(tracker.getsp(id)), (x, y-15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
        else:
            cv2.putText(roi, str(id) + " " + str(tracker.getsp(id)), (x, y-15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 3)

        s = tracker.getsp(id)
        if (tracker.f[id] == 1 and s != 0):
            tracker.capture(roi, x, y, h, w, s, id)

    # DRAW LINES 
    cv2.line(roi, (0, 410), (960, 410), (255, 0, 0), 2)
    cv2.putText(roi, 'START', (2, 425), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.line(roi, (0, 430), (960, 430), (255, 0, 0), 2)

    cv2.line(roi, (0, 235), (960, 235), (255, 0, 0), 2)
    cv2.putText(roi, 'END', (2, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.line(roi, (0, 255), (960, 255), (255, 0, 0), 2)

    # DISPLAY DATE, TIME, FPS & CURRENT FRAME
    cv2.line(roi, (0, 10), (960, 10), (79, 79, 47), 30)
    d = str(datetime.datetime.now().strftime("%d-%m-%y"))
    t = str(datetime.datetime.now().strftime("%H-%M-%S"))
    cv2.putText(roi, f'DATE: {d} |', (25, 19), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 255, 255), 2)
    cv2.putText(roi, f'TIME: {t} |', (209, 19), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 255, 255), 2)
    cv2.putText(roi, f'FPS: {fps} |', (393, 19), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 255, 255), 2)
    cv2.putText(roi, f'FRAMES: {frame_count} of {total_frames} ', (510, 19), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 255, 255), 2)
    cv2.line(roi, (0, 26), (960, 26), (255, 255, 255), 2)

    # DATA ALLOCATION
    ids_lst, spd_lst = tracker.dataset()

    # DISPLAY
    cv2.imshow("OUTPUT", roi)
    if cv2.waitKey(1) == 13:
        tracker.end()
        tracker.datavis(ids_lst, spd_lst)
        end = 1
        break

if(end != 1):
    tracker.end()

cap.release()
cv2.destroyAllWindows()
