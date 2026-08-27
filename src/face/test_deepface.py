from deepface import DeepFace

# Should match
result_match = DeepFace.verify(
    img1_path="data/authorized_faces/yogesh.jpg",
    img2_path="data/authorized_faces/yogesh_2.jpg",  # different photo, same person
    detector_backend="retinaface"
)
print("Same person test:", result_match["verified"])

# Should NOT match
result_no_match = DeepFace.verify(
    img1_path="data/authorized_faces/yogesh.jpg",
    img2_path="data/authorized_faces/other_person.jpg",
    detector_backend="retinaface"
)
print("Different person test:", result_no_match["verified"])
