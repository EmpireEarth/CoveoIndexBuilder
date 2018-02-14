import sys

NUMBER_OF_REQUESTS = 2536
TAG = '"results" : [ {'
END_TAG = ']'
TAG_SIZE = 15

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


printLine('Building index...\n')

sum = 1
for i in range(1, NUMBER_OF_REQUESTS + 1):
	response = open('responses/eachResponse/response' + str(i) + '.txt', 'r').read()
	tagPosition = response.find(TAG) + TAG_SIZE - 1
	response = response[tagPosition:]
	while True:
		nextBracket = response.find('{')
		nextBrace = response.find(']')
		if nextBracket == -1 or nextBracket > nextBrace:
			response = response[nextBrace+1:]
			break
		response = response[nextBracket:]
		for j, c in enumerate(response):
			if (response[j : j + 5] == '}, {\n') or (response[j : j + 24] == '} ],\n  "refinedKeywords"'):
				element = response[: j + 1]
				elementFile = open('responses/index/' + str(sum) + '.txt', 'w')
				appendToFile(element, elementFile)
				response = response[j + 1 :]
				printLine(str(sum))
				sum += 1
				elementFile.close()
				break

printLine('Done, ' + str(sum - 1) + ' elements created')