import cv2

def draw_hand_landmarks(
    frame,
    hand_landmarks,
    point_color=(0, 255, 0),
    line_color=(255, 0, 0),
    point_radius=5,
    line_thickness=2
    ):
    """
    image: frame OpenCV (BGR)
    hand_landmarks: lista de 21 landmarks normalizados (MediaPipe)
    """

    HAND_CONNECTIONS = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 7), (7, 8),
        (0, 9), (9, 10), (10, 11), (11, 12),
        (0, 13), (13, 14), (14, 15), (15, 16),
        (0, 17), (17, 18), (18, 19), (19, 20)
    ]

    h, w, _ = frame.shape

    # Converter landmarks normalizados para pixels
    points = []
    for hand in hand_landmarks:
        x = int(hand.x * w)
        y = int(hand.y * h)
        points.append((x, y))

    # Desenhar linhas
    for start, end in HAND_CONNECTIONS:
        cv2.line(
            frame,
            points[start],
            points[end],
            line_color,
            line_thickness
        )

    # Desenhar pontos
    for x, y in points:
        cv2.circle(
            frame,
            (x, y),
            point_radius,
            point_color,
            -1
        )