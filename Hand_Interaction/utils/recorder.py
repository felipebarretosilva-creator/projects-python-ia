import cv2


class Recorder:

    def __init__(self, output_path, fps, frame_size):

        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        self.writer = cv2.VideoWriter(
            output_path,
            fourcc,
            fps,
            frame_size
        )

    def write(self, frame):
        self.writer.write(frame)

    def release(self):
        self.writer.release()