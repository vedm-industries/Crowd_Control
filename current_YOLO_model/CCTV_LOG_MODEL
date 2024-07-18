import cv2
import numpy as np
from tracker import *  # Assuming tracker.py defines the Tracker class
import cvzone
import time

# Background subtractor for motion detection
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=140)

# Define counting regions (modify coordinates as needed)
area1 = [(213, 165), (200, 189), (693, 373), (697, 341)]  # Entry area
area2 = [(195, 199), (186, 213), (683, 404), (689, 388)]  # Exit area

# Variables for counting, logging, and time tracking
total_enter_count = 0
total_exit_count = 0
frame_count = 0
last_processed_frame = 0  # Track frame for periodic processing
processing_interval = 5  # Process frames and save results every 5 seconds
log_file_name = "people_count_log.txt"  # Adjust filename if desired

def update_log_file(enter_count, exit_count, timestamp):
    """
    Appends people count data to the log file.
    """
    with open(log_file_name, "a") as log_file:  # Open in append mode
        log_file.write(f"{timestamp}: Enter: {enter_count}, Exit: {exit_count}\n")

def get_current_timestamp():
    """
    Returns the current timestamp in a human-readable format.
    """
    return time.strftime("%H:%M:%S")

# Object tracker (assuming tracker.py defines the Tracker class)
tracker = Tracker()

# Live CCTV input (replace with appropriate code for your camera)
cap = cv2.VideoCapture(0)  # Change 0 to your camera ID if using a webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame (optional)
    frame = cv2.resize(frame, (1028, 500))

    # Background subtraction for motion detection
    mask = bg_subtractor.apply(frame)
    _, mask = cv2.threshold(mask, 245, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Track and classify objects
    object_list = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1500:
            object_list.append(cv2.boundingRect(cnt))
    bbox_idx = tracker.update(object_list)

    # Process objects and update counts
    enter_count = 0
    exit_count = 0
    for bbox in bbox_idx:
        x1, y1, x2, y2, id = bbox
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        # Check for entry and exit based on region intersections
        result_enter = cv2.pointPolygonTest(np.array(area1, np.int32), (cx, cy), False)
        result_exit = cv2.pointPolygonTest(np.array(area2, np.int32), (cx, cy), False)

        if result_enter >= 0:
            enter_count += 1

        if result_exit >= 0:
            exit_count += 1

        # Draw bounding box, ID, and update tracker
        cv2.rectangle(frame, (x1, y1), (x2 + x1, y2 + y1), (0, 255, 0) if id in tracker.tracked_objects else (0, 0, 255), 3)
        cvzone.putTextRect(frame, f"{id}", (cx, cy), 2, 2)
        tracker.update_status(id, (cx, cy))

    # Draw entry and exit regions
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,0,255),2) 
    cv2.polylines(frame,[np.array(area2,np.int32)],True,(0,0,255),2) 

    Enter=len(counter1)
    Exit=len(counter2)
    cvzone.putTextRect(frame,f'ENTER:-{Enter}',(50,60),2,2)
    cvzone.putTextRect(frame,f'EXIT:-{Exit}',(50,130),2,2)


    print(er)
    cv2.imshow('RGB', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
