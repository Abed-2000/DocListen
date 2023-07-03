import os
from gtts import gTTS
from PyPDF2 import PdfReader

script_path = os.path.dirname(os.path.abspath(__file__))

raw_path = os.path.join(script_path, "rawMedia")
processedMedia = os.path.join(script_path, "processedMedia")


file2Convert = input("Enter the name of the file that you would like to convert to an audio format. \n(Please ensure that the file exists within the \"rawMedia\" folder; ex. sample.txt or sample.pdf): ")

try:
    with open(os.path.join(raw_path, file2Convert)) as document:
        contents = document.read()
        tts = gTTS(contents, lang = 'bn')
        tts.save(os.path.join(processedMedia, (file2Convert + "_en.mp3")))

except FileNotFoundError:
    print('File does not exist in the \"rawMedia\" folder.')