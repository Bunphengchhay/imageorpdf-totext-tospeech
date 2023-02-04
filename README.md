# Image or PDF to text to Speech with python
## Purposes
### This is for demonstration purpose only. This python program will be used to convert image or pdf to text using tesseract and pytesseract. And then it will convert text to speech using gtts.

    Limitation
    This program is able to take .jpg | .png | .pdf only
## CLONE
    git clone git@github.com:Bunphengchhay/imageorpdf-totext-tospeech.git
## Requirements
### This program required Tersseract and Pytesseract
### The following command will used to install the required package.
     - pip install -r requirements.txt

## Image to text
    from PIL import Image
    import pytesseract
    def extract_text_from_image(image_file):
        # Open the image file
        image = Image.open(image_file)
        # Use pytesseract to extract text from image
        text = pytesseract.image_to_string(image)

        return text

### In this function we need to import Image from PIL. We use it to read the image file. This Image can only take .jpg and .png. And then we need to use pytesseract to read the image and return the text as a string.

## PDF to text
    import PyPDF2
    def extract_text_from_pdf(pdf_file):
        pdfFile = open(pdf_file, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        text = ""

        for i in range(len(pdfReader.pages)):
            page = pdfReader.pages[i]
            text += page.extract_text()

        return text

### Similarly, this function will use PyPDF2 to read the input from the handler. This function will take .pdf file and use for loop to read all the text (if more than one page) and return string as the output.

## Text to Speech
    from gtts import gTTS
    import os
    def convert_textToSpeech(text, language):
        # Create a gTTS object
        tts = gTTS(text=text, lang=language) 
        # Save the generated speech to a file
        tts.save("speech.mp3") 
        # Play the generated speech on mac
        os.system("afplay speech.mp3")

### This function will use gtts and os to convert text to speech. This function will take text and language as an input. You can specify any languages you like. Please refer to this link for more details over the use of language with gtts.
    https://gtts.readthedocs.io/en/latest/module.html

### After that we will save the audio result into the same main folder. The os.system will be using to to invoke the system call to read aloud the text for you.
