
# core/physics.py

class PhysicsEngine:

    def __init__(self):
        pass

    # ----------------------------
    # Bounding box
    # ----------------------------
    def bbox(self, rect):

        cx, cy = rect.center
        w, h = rect.size

        return (
            cx - w//2,
            cy - h//2,
            cx + w//2,
            cy + h//2)

    # ----------------------------
    # Collision detection
    # ----------------------------
    def is_colliding(self, r1, r2):

        ax1, ay1, ax2, ay2 = self.bbox(r1)
        bx1, by1, bx2, by2 = self.bbox(r2)

        return not (
            ax2 < bx1 or
            ax1 > bx2 or
            ay2 < by1 or
            ay1 > by2)

    # ----------------------------
    # Collision resolution
    # ----------------------------
    def resolve(self, r1, r2):

        ax1, ay1, ax2, ay2 = self.bbox(r1)
        bx1, by1, bx2, by2 = self.bbox(r2)

        overlap_x = min(ax2, bx2) - max(ax1, bx1)
        overlap_y = min(ay2, by2) - max(ay1, by1)

        if overlap_x < overlap_y:

            if r1.center[0] < r2.center[0]:
                r1.center[0] -= overlap_x//2
                r2.center[0] += overlap_x//2
            else:
                r1.center[0] += overlap_x//2
                r2.center[0] -= overlap_x//2

        else:

            if r1.center[1] < r2.center[1]:
                r1.center[1] -= overlap_y//2
                r2.center[1] += overlap_y//2
            else:
                r1.center[1] += overlap_y//2
                r2.center[1] -= overlap_y//2

    # ----------------------------
    # Global update
    # ----------------------------
    def update(self, rects):

        n = len(rects)

        for i in range(n):

            for j in range(i+1, n):

                if self.is_colliding(rects[i], rects[j]):
                    self.resolve(rects[i], rects[j])
