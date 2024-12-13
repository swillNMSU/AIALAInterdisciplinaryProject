from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO('runs/detect/train/weights/best.pt')  # Use the best weights from training

# Predict on a new video or image
results = model.predict(source='YogaDog.mp4', save=True)

# Print prediction results
for result in results:
    print("Bounding Boxes: ", result.boxes)  # Bounding boxes
    print("Confidence Scores: ", result.boxes.conf)  # Confidence scores
    print("Class IDs: ", result.boxes.cls)  # Predicted class IDs
