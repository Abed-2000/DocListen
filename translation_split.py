import os
import nltk

def split_translation_file(inputFile, outputLocation):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    file = open(inputFile, "r")
    data = file.read()
    sentences = tokenizer.tokenize(data)

    fileCount = 1
    currentChunk = ''
    currentCharCount = 0

    for sentence in sentences:
        sentenceLen = len(sentence) + 1
        if currentCharCount + sentenceLen > 15000 and currentChunk:
            output_file = os.path.join(outputLocation, f'translationData{fileCount}.txt')
            with open(output_file, 'w') as file:
                file.write(currentChunk)
            fileCount += 1
            currentChunk = ''
            currentCharCount = 0
        currentChunk += sentence + ' '
        currentCharCount += sentenceLen

    if currentChunk:
        output_file = os.path.join(outputLocation, f'translationData{fileCount}.txt')
        with open(output_file, 'w') as file:
            file.write(currentChunk)

    print(f'{fileCount} file(s) created.')
    return fileCount
