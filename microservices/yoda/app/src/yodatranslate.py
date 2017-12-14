import requests
import json
import os

googleNLPAPIKey = os.environ['NLP_API_KEY']
googleNLPUrl = 'https://language.googleapis.com/v1/documents:analyzeSyntax?key='+googleNLPAPIKey

def yodaTranslate(sentence):

    # This function makes use of Google Language API to Yoda translate your sentence

    sentence = cleanUpSentence(sentence)

    payload = {
      "encodingType": "UTF8",
      "document": {
        "type": "PLAIN_TEXT",
        "content": sentence
      }
    }
    response = requests.request("POST", googleNLPUrl, data=json.dumps(payload))
    print(response.json())
    tokens = response.json()["tokens"]

    index = -1
    verbIndex = -1
    sentenceObject = ''
    sentenceSubject = ''
    numOfWords = len(tokens)
    for token in tokens:
        index = index + 1
        if (verbIndex != -1):
            sentenceObject = sentenceObject + token["text"]["content"] + ' '
        else:
            sentenceSubject = sentenceSubject + token["text"]["content"] + ' '
        if (token["partOfSpeech"]["tag"] == 'VERB' and verbIndex == -1):
            verbIndex = index

    yodaSentence = sentenceObject + sentenceSubject

    if(tokens[index]["partOfSpeech"]["tag"] == 'VERB'):
        return 'Hmmm .. This sentence already seems yodified.'
    if (numOfWords < 4):
        return 'Yoda does not speak such short sentences'
    if (verbIndex < 1):
        return 'Does not seem to be a valid "Yodifyable" sentence.'
    else:
        resp = yodaSentence.capitalize()
        return resp

def cleanUpSentence(sentence):
	sentence = sentence.replace("n't", " not")
	sentence = sentence.replace("'ll", " will")
	sentence = sentence.replace("'s,", " is")
	sentence = sentence.replace("dont", "do not")
	sentence = sentence.replace("wont", "will not")