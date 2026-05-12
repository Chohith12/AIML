import cv2
import os

video_path = "video.mp4"
output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

count = 0
frame_id = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if count % 30 == 0:
        cv2.imwrite(f"{output_folder}/frame_{frame_id}.jpg", frame)
        frame_id += 1

    count += 1

cap.release()

print("Frames extracted successfully!")