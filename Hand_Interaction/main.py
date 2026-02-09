# main.py

import cv2

from config import *
from core.hand_tracker import HandTracker
from core.drag_rect import DragRect
from core.render import Renderer
from utils.geometry import landmark_distance
from core.physics import PhysicsEngine
from utils.recorder import Recorder


def main():

    tracker = HandTracker(MODEL_PATH, NUM_HANDS)
    renderer = Renderer(ALPHA_OVERLAY)

    rects = [
        DragRect((150,150), RECT_SIZE),
        DragRect((400,150), RECT_SIZE)
    ]

    physics = PhysicsEngine()

    cap = cv2.VideoCapture(CAMERA_INDEX)
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps == 0:
        fps = FPS_OUTPUT  # fallback do config

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    recorder = Recorder(
        "output.avi",
        fps,
        (frame_width, frame_height)
    )

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape

        result = tracker.process(frame)

        cursor = None

        if result.hand_landmarks:

            hand = result.hand_landmarks[0]

            renderer.draw_hand(frame, hand)

            dist, pos = landmark_distance(
                hand, w, h, 8, 12)

            if dist < 40:
                cursor = pos

        if cursor:

            for r in rects:
                r.update(cursor, SMOOTHING)

        # Atualizar física
        physics.update(rects)

        frame = renderer.draw_rectangles(frame, rects)

        cv2.imshow("Hand Interaction", frame)

        recorder.write(frame)

        key = cv2.waitKey(1)

        if key==ord('n'):

            import random

            x = random.randint(100, w-100)
            y = random.randint(100, h-100)

            rects.append(DragRect((x,y), RECT_SIZE))

        if key==27:
            break

    recorder.release()
    tracker.close()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


