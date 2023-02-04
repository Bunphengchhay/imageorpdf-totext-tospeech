from PIL import Image
import pytesseract

def extract_text_from_image(image_file):
    # Open the image file
    image = Image.open(image_file)
    # Use pytesseract to extract text from image
    text = pytesseract.image_to_string(image)

    return text