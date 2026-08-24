import cv2
from ultralytics import YOLO
import time

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("/mnt/d/Sentinel Mind/data/authorized_faces/Data 1.mp4")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Width: {width}, Height: {height}, FPS: {fps}")

if fps == 0 or fps != fps:  # catches 0 and NaN
    fps = 20.0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

frame_count = 0
max_frames = 100  # just for testing

while frame_count < max_frames:
    ret, frame = cap.read()
    if not ret:
        print(f"Frame read failed at frame {frame_count}")
        break
    results = model(frame, classes=[0])
    annotated = results[0].plot()
    out.write(annotated)
    frame_count += 1
    print(f"Frame {frame_count} captured")

cap.release()
out.release()
print(f"Done. Total frames written: {frame_count}")
