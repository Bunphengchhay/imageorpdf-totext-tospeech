import PyPDF2

def extract_text_from_pdf(pdf_file):
    pdfFile = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    text = ""

    for i in range(len(pdfReader.pages)):
        page = pdfReader.pages[i]
        text += page.extract_text()

    return text
