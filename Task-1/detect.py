from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.predict(source="final.mp4", save=True)