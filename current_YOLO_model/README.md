This code provides a people counting system for video footage or live CCTV input. It tracks people entering and exiting defined regions, logging the results to a text file.  Here's how to use it without needing programming knowledge:

1. Setting Up:

Download the provided code files (including tracker.py if applicable).
Make sure you have Python installed on your computer. Python is a free and popular programming language used for various tasks, including image processing. You can download it from https://www.python.org/downloads/.

2. Configuring the Code: Open the main code file (likely named people_count.py).
Locate the following sections and update them according to your needs:
area1 and area2: These lists define the coordinates of two rectangular regions. People crossing from area1 to area2 are counted as entering, and vice versa for exiting. Modify the coordinates (X1, Y1, X2, Y2) for each point to match your desired counting zones in the video/CCTV feed.
log_file_name: Change this to your preferred name for the text file that will store the count data.
Optional: The code resizes the video frame to a specific resolution (currently 1028x500). If you want to keep the original resolution, comment out the line frame = cv2.resize(frame, (1028, 500)).

3. Running the Code: Open a terminal or command prompt window (search for "cmd" in Windows or access it through your terminal application).
Navigate to the directory where you saved the code files using commands like cd (Windows) or cd followed by the path (e.g., cd Documents/people_counting).
Assuming Python is installed correctly and the code file is named people_count.py, execute the script using the command python people_count.py.


4. Using Live CCTV Input: If you want to use live CCTV footage instead of a video file, change the line cap = cv2.VideoCapture(0) to use your camera ID. Consult your CCTV system's documentation to find the appropriate camera ID (replace the 0 with the cam IP ID).

5. Viewing the Results: The code will display the video feed with bounding boxes around detected people and text indicating their IDs.
The people entering and exiting will be counted and periodically logged to the specified text file (log_file_name).

6. Stopping the Code: Press the Esc key on your keyboard to stop the program and close the window.

Additional Notes:
This is a basic implementation and may require adjustments depending on your specific video/CCTV setup and lighting conditions.
You MUST unzip/extract the store.zip file prior to running the model if you choose to use an .mp4
You MUST put the store.mp4, enext model.py, and tracker.py in the same folder prior to running the model


