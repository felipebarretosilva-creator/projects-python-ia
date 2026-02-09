import cv2

def recorder(cap, frame):
    # Recording
    cap_weight = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20.0

    #Define codec (FourCC) and VideoWriter
    fourcc = cv2.VideoWriter.fourcc(*"MJPG")  # Use 'MP4V' or 'MJPG'
    out = cv2.VideoWriter('video_gravado.avi', fourcc, fps, (cap_weight, cap_height))
    out.write(frame)