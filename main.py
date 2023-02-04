import imagetotext
import pdftotext
import texttospeech

if __name__ == '__main__':
    print("Hello World")
    
    def extract_text(file):
      
        if file.endswith(".pdf"):
                # Call the extract_text_from_pdf function if the file is a PDF
            return pdftotext.extract_text_from_pdf(file)
        elif file.endswith(".jpg") or file.endswith(".png"):
                # Call the extract_text_from_image function if the file is an image
            return imagetotext.extract_text_from_image(file)
        else:
                # If the file type is not supported, return an error message
            return "File type not supported. Please provide a PDF or image file."



    #file = './artifact/imagesample.png'
    file = './artifact/sample.pdf'
    text = extract_text(file)
    print(text)
    # set language and call text to speech funtion
    language = 'en'
    texttospeech.convert_textToSpeech(text, language)

