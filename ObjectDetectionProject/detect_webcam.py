from ultralytics import YOLO
import cv2

def main():
    print("Loading YOLO model...")
    model = YOLO("yolov8n.pt")

    print("Opening webcam...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.5)
        annotated_frame = results[0].plot()

        cv2.imshow("YOLO Webcam Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
