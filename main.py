import os
from gtts import gTTS
from PyPDF2 import PdfReader
import langcodes

script_path = os.path.dirname(os.path.abspath(__file__))

rawMedia = os.path.join(script_path, "rawMedia")
processedMedia = os.path.join(script_path, "processedMedia")
temp = os.path.join(script_path, "temp")

def is_valid_language_code(code):
    try:
        langcodes.Language.get(code)
        return True
    except langcodes.LanguageTagError:
        return False

def get_valid_language_code():
    while True:
        language_code = input("\nEnter the language that you wish for the final translation to be in;\n(ex. for english type \"en\" or for french type \"fr\"): ").strip()
        if is_valid_language_code(language_code):
            return language_code
        else:
            print("Invalid language code. Please try again.")

file2Convert = input("Enter the name of the file that you would like to convert to an audio format. \n(Please ensure that the file exists within the \"rawMedia\" folder; ex. sample.txt or sample.pdf): ")
valid_language_code = get_valid_language_code()
os.environ["languageCode"] = valid_language_code

try:
    with open(os.path.join(rawMedia, file2Convert)) as document:
        contents = document.read()
        tts = gTTS(contents, lang = valid_language_code)
        tts.save(os.path.join(processedMedia, (file2Convert + "_" + valid_language_code + ".mp3")))
except FileNotFoundError:
    print('File does not exist in the \"rawMedia\" folder.')