from PIL import Image
import pytesseract

import snapping_tool

import os

class Snipping:
    def work_snipping():
        os.system('python snapping_tool.py')


class Ocr_Demo:

    def image_to_text():
                
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

        im = Image.open("capture.png")

        text = pytesseract.image_to_string(im)

        tx_file = open("tet.txt",'w')        # use w to write and if no exist it creat txt file as it name
        tx_file.write(text)                  # write function to write a line
        tx_file.close()                      #we need to close function unless it cann't finish process

        # print(text)

        import subprocess as sp
        programName = "notepad.exe"
        fileName = "tet.txt"
        sp.Popen([programName, fileName])




if __name__ == '__main__':
    Snipping.work_snipping()
    Ocr_Demo.image_to_text()