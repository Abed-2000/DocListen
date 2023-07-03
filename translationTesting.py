import os
from googletrans import Translator
from translation_split import split_translation_file

scriptPath = os.path.dirname(os.path.abspath(__file__))
rawPath = os.path.join(scriptPath, "rawMedia")
tempPath = os.path.join(scriptPath, "temp")
processedMedia = os.path.join(scriptPath, "processedMedia")
tranlationNeededFile = os.path.join(rawPath, "shortStory")

translator = Translator()


        
numTranslationFiles = split_translation_file(tranlationNeededFile, tempPath)

directory = tempPath
 
for filename in os.scandir(directory):
    if filename.is_file():
        with open(filename.path, "r") as file:
            translationData = file.read()
            translation = translator.translate(translationData, dest='bn')
            finalTranslation = open(os.path.join(rawPath, "translatedText.txt"), "w")
            finalTranslation.write(translation.text)