from ultralytics import YOLO
import cv2

# Paths
model_path = "./your_folder/yolov8s.pt" 
image_path = "./your_folder/your_image.jpg" #or .png

#Load the model
model = YOLO(model_path)

#Run inference
results = model(image_path)  

#Get the first result (your image)
result = results[0]

# Extract the image with the bounding boxes drawn (ready for OpenCV)
annotated_frame = result.plot()  # This returns an OpenCV compatible numpy array

# Show image with OpenCV
cv2.imshow("YOLOv8 Detection", annotated_frame)

# Wait for a key press before closing
print("Press any key on the keyboard to close the window.")
cv2.waitKey(0)

# Close the windows
cv2.destroyAllWindows()
