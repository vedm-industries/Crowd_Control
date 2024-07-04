import cv2
from ultralytics import YOLO  

# Path to  YOLO model weights
model_path = "yolov10s.pt"  # Replace with model path

# Path to class names file
class_names_path = "coco.txt"

# Load YOLO model
model = YOLO(model_path)

# Read class names
with open(class_names_path, "r") as f:
    class_names = f.read().strip().split("\n")


def extract_people_detections(results, class_names, confidence_threshold=0.5):
    """
    Extracts detections for the 'person' class from YOLO results.

    Args:
        results: The output from the YOLO model (could be a list or dictionary).
        class_names: A list of class names for the model.
        confidence_threshold: Minimum confidence threshold for detections (default: 0.5).

    Returns:
        list: A list of detections for the 'person' class, where each detection is a dictionary
              with the following keys:
                - x1: Integer (bounding box top-left X coordinate).
                - y1: Integer (bounding box top-left Y coordinate).
                - x2: Integer (bounding box bottom-right X coordinate).
                - y2: Integer (bounding box bottom-right Y coordinate).
                - confidence: Float (detection confidence score).
    """

    people_detections = []
    if isinstance(results, list):  # Check if results is a list
        # Assuming each element in the list is a detection
        for detection in results:
            try:
                x1, y1, x2, y2, conf, class_id, name = detection
            except ValueError:  # Handle potential unpacking error
                print("Warning: Unexpected detection format. Skipping...")
                continue
            class_name = class_names[int(class_id)]
            if class_name == "person" and conf > confidence_threshold:  # Only consider "person" class
                people_detections.append({
                    "x1": int(x1),
                    "y1": int(y1),
                    "x2": int(x2),
                    "y2": int(y2),
                    "confidence": float(conf)
                })
    elif isinstance(results, dict):  # Check if results is a dictionary
        # Assuming results structure based on Ultralytics output 
        for value in results.values():
            if isinstance(value, list):  # Check if value is a list of detections
                for detection in value:
                    try:
                        x1, y1, x2, y2, conf, class_id, name = detection
                    except ValueError:  # Handle potential unpacking error
                        print("Warning: Unexpected detection format. Skipping...")
                        continue
                    class_name = class_names[int(class_id)]
                    if class_name == "person" and conf > confidence_threshold:  # Only consider "person" class
                        people_detections.append({
                            "x1": int(x1),
                            "y1": int(y1),
                            "x2": int(x2),
                            "y2": int(y2),
                            "confidence": float(conf)
                        })
    else:
        print("WARNING: Unexpected YOLO results format. Please check model output structure.")

    return people_detections


# Video capture 
cap = cv2.VideoCapture('cctv.mp4')

# Counting line coordinates )
cy1 = 364
frame_width = 1020

# Loop through video frames
while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    # Assuming frame width is 1020
    new_width = 1020
    aspect_ratio = float(frame.shape[1]) / frame.shape[0] # Width / Height
    
    # Calculate new height to maintain aspect ratio
    new_height = int(new_width / aspect_ratio)

    # Resize frame
    frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Get detections from YOLO model
    results = model(frame)

    # Extract people detections
    people_detections = extract_people_detections(results, class_names)

    # Count people 
    people_count = len(people_detections)
    print(f"Number of people detected: {people_count}")

    # Draw counting line and display frame
    cv2.line(frame, (3, cy1), (frame_width, cy1), (255, 255, 255), 1)  # Counting line
    cv2.imshow('People Counting', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
