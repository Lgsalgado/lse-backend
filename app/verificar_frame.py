import cv2

cap = cv2.VideoCapture("dataset/buenos_dias/buenos_dias_01.mp4")
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Frames en el video: {frame_count}")
cap.release()
