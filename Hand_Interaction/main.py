# main.py

import cv2

from config import *
from core.hand_tracker import HandTracker
from core.drag_rect import DragRect
from core.render import Renderer
from utils.geometry import landmark_distance
from core.physics import PhysicsEngine
from utils.recorder import recorder


def main():

    cap = cv2.VideoCapture(CAMERA_INDEX)

    tracker = HandTracker(MODEL_PATH, NUM_HANDS)
    renderer = Renderer(ALPHA_OVERLAY)

    rects = [
        DragRect((150,150), RECT_SIZE),
        DragRect((400,150), RECT_SIZE)
    ]

    physics = PhysicsEngine()

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

        recorder(cap, frame)

        key = cv2.waitKey(1)

        if key==ord('n'):

            import random

            x = random.randint(100, w-100)
            y = random.randint(100, h-100)

            rects.append(DragRect((x,y), RECT_SIZE))

        if key==27:
            break

    tracker.close()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


