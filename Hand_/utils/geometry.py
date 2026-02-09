# utils/geometry.py

import math


def landmark_distance(hand, w, h, i1, i2):

    p1 = hand[i1]
    p2 = hand[i2]

    x1 = p1.x * w
    y1 = p1.y * h

    x2 = p2.x * w
    y2 = p2.y * h

    return math.dist((x1,y1),(x2,y2)), (
        int((x1+x2)/2),
        int((y1+y2)/2)
    )
