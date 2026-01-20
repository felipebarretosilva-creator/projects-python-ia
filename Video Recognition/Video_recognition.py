"""
Code development: January 26th.

This code works within mediapipe 0.10.31, where solutions package is no longer available and, as far as I know, Task method does not have a support for drawing into frame.

This solution works alongside a function called "draw_function" to plot all points manually into videocam, using cv2 library.

I ran this solution with python version 3.13 and mediapipe version 0.10.31, and it worked fine.

hand_landmarks.taks must be downloaded from Media Pipe documentation, see: https://ai.google.dev/edge/mediapipe/solutions
"""

import cv2
import mediapipe as mp
from draw_function import draw_hand_landmarks

#Inital Parameters
task_path = r'C:\yourpath...\hand_landmarker.task'
camera = 0 #if you have more than one webcam, you can select one by change this number.

#--- MODEL CONFIGURATION ---
#Create an HandLandmarker object.
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a recognizer instance with the video mode:
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=task_path),
    num_hands=2,
    running_mode=VisionRunningMode.VIDEO)

with HandLandmarker.create_from_options(options) as landmarker:
    #webcam into python
    cam = cv2.VideoCapture(camera)

    #Cam Connection
    if cam.isOpened():
        validacao, frame = cam.read()
        frame_counter = 0

        while validacao:
            #Capture frames
            validacao, frame = cam.read()

            # Convert the frame received from OpenCV to a MediaPipe’s Image object.
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

            #Task: Hand detection for video
            results = landmarker.detect_for_video(mp_image, frame_counter)

            if results.hand_landmarks:
                for landmark in results.hand_landmarks:
                    draw_hand_landmarks(frame, landmark)

            #New window with cam capture
            cv2.imshow('Video', frame)

            #Python waiting process
            tecla = cv2.waitKey(2)
            frame_counter += 200

            # Stop code if "ESC" is pressed
            if tecla == 27:
                break

#release cam and close window
cam.release()
cv2.destroyAllWindows()