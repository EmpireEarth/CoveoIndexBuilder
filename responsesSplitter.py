import json
import sys

NUMBER_OF_REQUESTS = 2559

def printLine(str):
	sys.stdout.write(str + '\n')
	sys.stdout.flush()

def appendToFile(objects, file, sep='', end=''):
	enc = file.encoding
	if enc == 'UTF-8':
		print(*objects, sep=sep, end=end, file=file)
	else:
		f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
		print(*map(f, objects), sep=sep, end=end, file=file)


printLine('Splitting responses...\n')

with open('responses/allResponses.txt', 'r') as responsesFile:
    responses = responsesFile.read()

tag = responses[:18];
i = 1
while True:
	title = 'response' + str(i)
	resultsTagPosition1 = responses.find(tag)
	resultsTagPosition2 = responses.find(tag, resultsTagPosition1 + 1)
	if resultsTagPosition2 == -1:
		response = responses[resultsTagPosition1:].rstrip()
		responseFile = open('responses/eachResponse/' + title + '.txt', 'w')
		appendToFile(response, responseFile)
		printLine('File created : ' + title)
		break
	else:
		response = responses[resultsTagPosition1:resultsTagPosition2].rstrip()
		responseFile = open('responses/eachResponse/' + title + '.txt', 'w')
		appendToFile(response, responseFile)
		printLine('File created : ' + title)
		responses = responses[resultsTagPosition2:]
	i += 1

printLine('Done, ' + str(i) + 'files created')