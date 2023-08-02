import os
from googletrans import Translator
from translation_split import split_translation_file

scriptPath = os.path.dirname(os.path.abspath(__file__))
rawMedia = os.path.join(scriptPath, "rawMedia")
temp = os.path.join(scriptPath, "temp")
processedMedia = os.path.join(scriptPath, "processedMedia")
tranlationNeededFile = os.path.join(rawMedia, "shortStory")
languageCode = os.environ["languageCode"]
translator = Translator()

numTranslationFiles = split_translation_file(tranlationNeededFile, temp)

directory = temp
 
for filename in os.scandir(directory):
    if filename.is_file():
        with open(filename.path, "r") as file:
            translationData = file.read()
            translation = translator.translate(translationData, dest=languageCode)
            finalTranslation = open(os.path.join(rawMedia, "translatedText.txt"), "w")
            finalTranslation.write(translation.text)