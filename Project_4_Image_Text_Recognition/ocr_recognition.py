import cv2
import pytesseract
import os

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Full image path
image_path = (
r"C:\Users\AKSHAYA SADASIVAN\OneDrive\Desktop\decodelabs_tasks\Project 4 Image Text Recognition\sample_text.jpeg"
)

# Check file exists
if not os.path.exists(image_path):
    print("Image not found!")
    exit()

# Read image
image = cv2.imread(image_path)

# Convert
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

# OCR
text = pytesseract.image_to_string(gray)

print("\nDetected Text:\n")
print(text)