import cv2
import cv2.dnn_superres as dnn_superres
import os

print(cv2.__version__)

# Create super resolution object
sr = dnn_superres.DnnSuperResImpl_create()

# Model file (must exist in this folder)
model_path = "FSRCNN_x2.pb"
sr.readModel(model_path)

# Set model
sr.setModel("fsrcnn", 2)

# Read image
image = cv2.imread("1.jpg")

# Upscale
result = sr.upsample(image)

# Save output
cv2.imwrite("upscaled_image.png", result)