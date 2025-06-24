# YOLOv8 Image Detection Project

This project uses the YOLOv8 model to detect objects in a single image and count how many instances of a specific class (e.g., people) are present.

## 🧾 Description
The script loads a pre-trained YOLOv8 model (`yolov8s.pt`) and performs object detection on an input image. It identifies all detected objects and counts how many times a specific class appears (e.g., class 0 = 'person').

## 📦 Dependencies
Make sure you have the following libraries installed:
- `ultralytics`: For using the YOLOv8 model.
- `opencv-python` (optional): For displaying or saving annotated images.

Install them via pip:

```bash
pip install ultralytics opencv-python
```

## 📁 Folder Structure

```bash
image_detection_project/
│
├── yolov8s.pt              # Pre-trained YOLOv8 model
├── immagine.png            # Input image for detection
├── detect_objects.py       # Main script
└── README.md
```
## 🚀 How to Use
1. Place your image in the same directory as the script.
2. Make sure the YOLO model file (yolov8s.pt) is available.
3. Run the script:

```bash
python detect_objects.py
```
4. The output will show the number of detected objects of a given class (e.g., people).

> ⚠️ You can change the class index in the code if you want to count different types of objects.

## 📝 Notes
- Detected classes are printed in numeric form by default.
- To get class names (like "person", "car", etc.), use `model.names`.
```
