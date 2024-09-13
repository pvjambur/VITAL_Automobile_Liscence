from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import easyocr
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the model from the file
# model4 = load_model('path_to_your_model.h5')


# Initialize video capture
cap = cv2.VideoCapture("carvid.mp4")

# Load YOLO models
model = YOLO("yolov8n.pt")
model2 = YOLO("best.pt")
model3 = YOLO("lice.pt")

# Class names for YOLO models
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
classNames_np = ["NumberPlate"]

# Initialize EasyOCR reader once
reader = easyocr.Reader(['en'])

# Variables for calculating FPS
prev_frame_time = 0

while True:
    success, img = cap.read()
    if not success:
        break  # Break if no frame is read

    # Detect objects using YOLO models
    results = model(img, stream=True)
    results2 = model3(img, stream=True)

    # Process number plates
    for r in results2:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            conf = math.ceil((box.conf[0] * 100)) / 100
            crop_img = img[max(0, y1 - 20):min(y1 + 20 + h, img.shape[0]),
                       max(0, x1 - 20):min(x1 + 20 + w, img.shape[1])]

            outs = reader.readtext(crop_img)
            text = outs[0][1] if outs else "Unreadable"
            cvzone.putTextRect(img, f'NumberPlate {conf} {text}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

    # Process other objects
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1
            cls = int(box.cls[0])
            if classNames[cls] == "car" or classNames[cls] == "bus" or classNames[cls] == "truck":
                crop_img = img[y1:y1 + h, x1:x1 + w]
                finalpart = model2(crop_img)
                ans = finalpart[0].names[finalpart[0].probs.top1]
                conf = math.ceil((box.conf[0] * 100)) / 100
                cvzone.cornerRect(img, (x1, y1, w, h))
                cvzone.putTextRect(img, f'{classNames[cls]} {conf} {ans}', (max(0, x1), max(35, y1)), scale=1,
                                   thickness=1)

    # Calculate FPS
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(f"FPS: {fps:.2f}")

    # Display the image
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
