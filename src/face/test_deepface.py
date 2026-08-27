from deepface import DeepFace

result = DeepFace.verify(
    img1_path="data/authorized_faces/yogesh.jpg",
    img2_path="data/authorized_faces/yogesh.jpg",
    detector_backend="retinaface"  # or "mtcnn", "mediapipe"
)
print(result)
