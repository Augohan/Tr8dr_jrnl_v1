import cv2

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise
    denoised_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    return denoised_image
