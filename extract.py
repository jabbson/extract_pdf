import os 
import re
import PyPDF2

current_dir = os.path.dirname(os.path.realpath(__file__))
pdfs_path = os.path.join(current_dir, 'pdf_collection')
pdfs_names = os.listdir(pdfs_path)

for p in pdfs_names:
    pdfFileObj = open(os.path.join(pdfs_path, p), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()

    line = re.search(r'>(.*)<', text)
    if line:
        print(line.group(1))