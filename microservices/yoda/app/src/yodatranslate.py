from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six


def yodaTranslate(text):
	client = language.LanguageServiceClient()

	if isinstance(text, six.binary_type):
	    text = text.decode('utf-8')

	# Instantiates a plain text document.
	# [START migration_analyze_syntax]
	document = types.Document(
	    content=text,
	    type=enums.Document.Type.PLAIN_TEXT)

	# Detects syntax in the document. You can also analyze HTML with:
	#   document.type == enums.Document.Type.HTML
	tokens = client.analyze_syntax(document).tokens

	# part-of-speech tags from enums.PartOfSpeech.Tag
	pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
	           'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

	i = -1
	verbIndex = -1
	sentenceObject = ''
	sentenceSubject = ''
	for token in tokens:
		i = i + 1
		if (verbIndex != -1):
			sentenceObject = sentenceObject + '{} '.format(token.text.content)
		else:
			sentenceSubject = sentenceSubject + '{} '.format(token.text.content)
		if (pos_tag[token.part_of_speech.tag] == 'VERB' and verbIndex == -1):
			verbIndex = i


	yodaSentence = sentenceObject + sentenceSubject

	resp = yodaSentence.capitalize()
	return resp