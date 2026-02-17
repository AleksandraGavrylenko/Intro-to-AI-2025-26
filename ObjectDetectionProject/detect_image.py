from ultralytics import YOLO
import cv2

def main():
    print("Loading YOLO model...")
    model = YOLO("yolov8n.pt")  # Downloads automatically first time

    image_path = "sample_image.jpg"

    print("Reading image...")
    image = cv2.imread(image_path)

    if image is None:
        print("Error: sample_image.jpg not found.")
        return

    print("Running object detection...")
    results = model(image, conf=0.5)

    annotated_image = results[0].plot()

    cv2.imshow("YOLO Object Detection", annotated_image)
    cv2.imwrite("output_detected.jpg", annotated_image)

    print("Detection complete.")
    print("Saved as output_detected.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
