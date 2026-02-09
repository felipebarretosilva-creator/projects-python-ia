# core/renderer.py

import cv2
import numpy as np


HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (0,9),(9,10),(10,11),(11,12),
    (0,13),(13,14),(14,15),(15,16),
    (0,17),(17,18),(18,19),(19,20)
]


class Renderer:

    def __init__(self, alpha=0.5):

        self.alpha = alpha


    def draw_hand(self, frame, landmarks):

        h, w, _ = frame.shape

        points = []

        for lm in landmarks:
            points.append((
                int(lm.x*w),
                int(lm.y*h)
            ))

        for s,e in HAND_CONNECTIONS:
            cv2.line(frame, points[s], points[e], (255,255,255), 2)

        for x,y in points:
            cv2.circle(frame, (x,y), 4, (0,255,0), -1)


    def draw_rectangles(self, frame, rects):

        overlay = np.zeros_like(frame)

        for rect in rects:

            cx, cy = rect.center
            w, h = rect.size

            cv2.rectangle(
                overlay,
                (cx-w//2, cy-h//2),
                (cx+w//2, cy+h//2),
                rect.color(),
                -1
            )

        return cv2.addWeighted(
            overlay,
            self.alpha,
            frame,
            1-self.alpha,
            0
        )
