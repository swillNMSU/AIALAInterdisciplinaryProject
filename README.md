# YOLOv8 Animal Behavior Detection

This project trains and tests a YOLOv8 model to detect animal behavior in videos. The dataset was created by annotating frames extracted from videos, and the YOLO model was fine-tuned on this custom dataset.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Setup](#setup)
4. [Training the Model](#training-the-model)
5. [Testing the Model](#testing-the-model)
6. [Results](#results)
7. [File Structure](#file-structure)
8. [Credits](#credits)

---

## **Project Overview**
The goal of this project is to utilize YOLOv8 for detecting animal behavior in videos. The workflow includes:
- Preparing the dataset by annotating video frames.
- Training the YOLOv8 model on the annotated dataset.
- Testing the model on new data (images/videos).
- Analyzing the results.

---

## **Requirements**
### **Tools and Libraries**
1. **Python** (3.8+)
2. Required Python libraries:
   - `ultralytics`
   - `opencv-python`
   - `matplotlib`
   - `numpy`
3. **YOLOv8 Pre-trained Weights** (automatically downloaded during training).

### **Installation**
Run the following command to install the required libraries:
pip install ultralytics opencv-python matplotlib numpy

# Setup

## 1. Dataset Structure
Ensure your dataset follows this structure:
dataset/
├── train/
│   ├── images/  # Training images
│   ├── labels/  # YOLO-format label files
├── val/
│   ├── images/  # Validation images
│   ├── labels/  # YOLO-format label files


## 2. dataset.yaml File
Create a dataset.yaml file in the root directory:

train: dataset/train/images
val: dataset/val/images

nc: 1  # Number of classes
names: ['animal']  # Replace with your class names

# Training the Model
Run the train_yolo.py script:

The training process:
Uses YOLOv8 pre-trained weights.
Fine-tunes the model on your custom dataset.
The best-trained weights are saved in the runs/detect/train directory.
Testing the Model
Run the test_yolo.py script to test the model on new images or videos:

bash
Copy code
python test_yolo.py
Modify the source argument in the script to test specific files:
Images: Provide the path to a test image (e.g., path/to/test/image.jpg).
Videos: Provide the path to a test video (e.g., path/to/test/video.mp4).
Results will be saved in the runs/detect/predict directory.

# Results
Output results include:

Annotated images with bounding boxes.
Annotated videos showing detections.
View example results in the runs/detect/predict folder.
File Structure
Ensure your project directory is structured as follows:

project/
├── dataset/
│   ├── train/
│   │   ├── images/
│   │   ├── labels/
│   ├── val/
│   │   ├── images/
│   │   ├── labels/
├── train_yolo.py        # Script for training the YOLOv8 model
├── test_yolo.py         # Script for testing the trained YOLOv8 model
├── dataset.yaml         # Configuration file for YOLO dataset
├── README.md            # Project documentation
