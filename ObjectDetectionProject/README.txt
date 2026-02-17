Object Detection Project (Python + YOLOv8)

SETUP INSTRUCTIONS:

1) Open this folder in Visual Studio or VS Code.
2) Open Terminal inside the folder.
3) Install required packages:

   pip install -r requirements.txt

4) Run image detection:

   python detect_image.py

5) Run webcam detection:

   python detect_webcam.py

Press Q to quit webcam mode.

If webcam does not open, change:
    cv2.VideoCapture(0)
to:
    cv2.VideoCapture(1)
