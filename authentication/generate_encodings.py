import face_recognition
import pickle
import os

FACE_FOLDER = "static/faces"

known_encodings = []
known_names = []

for user in os.listdir(FACE_FOLDER):

    user_folder = os.path.join(FACE_FOLDER, user)

    if not os.path.isdir(user_folder):
        continue

    for image_name in os.listdir(user_folder):

        image_path = os.path.join(user_folder, image_name)

        image = face_recognition.load_image_file(image_path)

        encodings = face_recognition.face_encodings(image)

        if len(encodings) == 0:
            print(f"No face found in {image_name}")
            continue

        known_encodings.append(encodings[0])
        known_names.append(user)

print(f"Loaded {len(known_encodings)} face encodings.")

data = {
    "encodings": known_encodings,
    "names": known_names
}

os.makedirs("authentication", exist_ok=True)

with open("authentication/encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("Face encodings saved successfully.")