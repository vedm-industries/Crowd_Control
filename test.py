import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO



model=YOLO('yolov8s.pt')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture('vidyolov8.mp4')

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
print(class_list)
count=0
while True:
    
    ret,frame = cap.read()
    frame=cv2.resize(frame,(1020,500))
    if ret is None:
        break
    count += 1
    if count % 5 != 0:
        continue

    results=model.predict(frame) #draws bounding box
    # print(results)
    akin=results[0].boxes.xyxy #bounding box info with class and confidence
    # print(akin)
    pltx=pd.DataFrame(akin).astype("float") #converts information in panda
    # print(pltx)
    for index,row in pltx.iterrows():
        # print(row)
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        if 4 in row.index:
            d=int(row[4]) # class ID
            c=class_list[d]
        else:
            pass
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.putText(frame,str(c),(x1,y1),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)
        cv2.imshow("RGB", frame)
        if cv2.waitKey(0)&0xFF==27:
            break

cap.release()
cv2.destroyAllWindows()
