import cv2
import numpy as np
import pandas as pd

class YOLOv8:
    def __init__(self, model_path):
        self.model = cv2.dnn.readNet(model_path)
        self.classes = []

    def load_classes(self, classes_file):
        with open(classes_file, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]

    def detect_objects(self, frame):
        height, width = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.model.setInput(blob)
        outputs = self.model.forward(self.model.getUnconnectedOutLayersNames())

        boxes, confidences, class_ids = [], [], []
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        return [(boxes[i], class_ids[i]) for i in indices.flatten()]

def export_to_csv(detections, filename):
    df = pd.DataFrame(detections, columns=['Bounding Box', 'Class ID'])
    df.to_csv(filename, index=False)

if __name__ == '__main__':
    model_path = 'yolov8.weights'
    classes_file = 'coco.names'
    video_source = 0  # Change to video file path if required
    output_csv = 'detections.csv'

    yolo = YOLOv8(model_path)
    yolo.load_classes(classes_file)

    cap = cv2.VideoCapture(video_source)
    detections_list = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detections = yolo.detect_objects(frame)
        detections_list.extend(detections)
        # Display detections or process them as needed

    export_to_csv(detections_list, output_csv)
    cap.release()