# core/drag_rect.py

class DragRect:

    def __init__(self, center, size):

        self.center = list(center)
        self.size = size
        self.active = False
        self.grabbed = False

    def contains(self, point):

        cx, cy = self.center
        w, h = self.size

        return (
            cx-w//2 < point[0] < cx+w//2 and
            cy-h//2 < point[1] < cy+h//2
        )

    def update(self, cursor, smooth=0.3):

        if cursor and self.contains(cursor):

            self.grabbed = True
            self.active = True

            cx, cy = self.center

            self.center[0] = int(cx + (cursor[0]-cx)*smooth)

            self.center[1] = int(cy + (cursor[1]-cy)*smooth)

        else:
            self.grabbed = False
            self.active = False

    def color(self):

        return (0,255,0) if self.active else (255,0,255)
