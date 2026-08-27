import cv2
from ultralytics import YOLO
from deepface import DeepFace
import time
import os

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("data/test_clips/P1E_S1_C1_0001.mp4")
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_face_id.mp4', fourcc, 10.0, (width, height))

AUTHORIZED_DIR = "data/authorized_faces"
AUTHORIZED_IMAGES = [os.path.join(AUTHORIZED_DIR, f) for f in os.listdir(AUTHORIZED_DIR)]

def identify_person(crop):
    for ref_img in AUTHORIZED_IMAGES:
        try:
            result = DeepFace.verify(
                img1_path=ref_img,
                img2_path=crop,
                detector_backend="retinaface",
                enforce_detection=False  # don't crash if no face found in crop
            )
            if result["verified"]:
                return "Authorized"
        except Exception:
            continue
    return "Unknown"

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print(f"Video ended at frame {frame_count}")
        break

    results = model(frame, classes=[0])
    boxes = results[0].boxes

    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        crop = frame[y1:y2, x1:x2]

        if crop.size == 0:
            continue

        label = identify_person(crop)
        color = (0, 255, 0) if label == "Authorized" else (0, 0, 255)

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    out.write(frame)
    frame_count += 1
    print(f"Frame {frame_count}: {len(boxes)} person(s) detected")

cap.release()
out.release()
print(f"Done. Total frames processed: {frame_count}")
