from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO('yolov8n.pt') 

# Train the model
model.train(
    data='dataset.yaml',  # Path to dataset.yaml
    epochs=3,             # Number of training epochs
    imgsz=640,            # Image size
    batch=16,             # Batch size
    workers=4             # Number of data loader workers
)

# Validate the model
val_results = model.val()

# Access specific metrics directly
print(f"Precision: {val_results.box.map50:.2f}")
print(f"mAP@0.5: {val_results.box.map50:.2f}")
print(f"mAP@0.5-0.95: {val_results.box.map:.2f}")

# For class-wise metrics, loop through results
for class_id, class_results in enumerate(val_results.box.maps):
    print(f"Class {class_id}: mAP = {class_results:.2f}")
