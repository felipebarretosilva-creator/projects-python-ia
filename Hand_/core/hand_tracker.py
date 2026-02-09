# core/hand_tracker.py

import cv2
import time
import mediapipe as mp


class HandTracker:

    def __init__(self, model_path, num_hands=1):

        BaseOptions = mp.tasks.BaseOptions
        HandLandmarker = mp.tasks.vision.HandLandmarker
        HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
        RunningMode = mp.tasks.vision.RunningMode

        options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            num_hands=num_hands,
            running_mode=RunningMode.VIDEO
        )

        self.landmarker = HandLandmarker.create_from_options(options)

        self.start_time = time.time()

    def process(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        timestamp = int(
            (time.time() - self.start_time) * 1000
        )

        return self.landmarker.detect_for_video(
            mp_image,
            timestamp
        )

    def close(self):
        self.landmarker.close()
