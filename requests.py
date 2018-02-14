import requests
import sys

URL = 'https://platform.cloud.coveo.com/rest/search/v2/'
HEADERS = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJmaWx0ZXIiOiJAc291cmNlPT0oQW5zd2Vyc0Nsb3VkLENvdmVvT25Zb3VUdWJlLENvdmVvVGFnZ2VkU2l0ZWNvcmVTdGFja0V4Y2hhbmdlLEpzU2VhcmNoUmVmLG9oY2VzNjVlbixvaGNlczY1ZnIsb2hjZXM3MGVuLG9oY2VzNzBmcixvaGNsb3VkZW4sb2hjbG91ZGZyLFRlY2hCbG9nLFwiU2FsZXNmb3JjZSBTZWN1cmVkIEl0ZW1zXCIpIE9SIChAc291cmNlPT0oZGV2ZWxvcGVycykgQHN5c2ZpbGV0eXBlPT0oY2ZwYWdlLHBkZikgTk9UIEBjZnNwYWNla2V5PT0oSnNTZWFyY2gsU2FsZXNmb3JjZSkpIE9SICgoQHNvdXJjZT09XCJTYWxlc2ZvcmNlIFB1YmxpYyBJdGVtc1wiIE5PVCBAc2Zpc3Zpc2libGVpbnBrYj1mYWxzZSkgT1IgKEBvYmplY3R0eXBlPT0oXCJGQVFcIixcIkhvdyBUb1wiLFwiS0IgQXJ0aWNsZVwiLFwiQmVzdCBQcmFjdGljZVwiKSBOT1QgQHNmaXN2aXNpYmxlaW5wa2I9ZmFsc2UpKSIsInVzZXJHcm91cHMiOlsic3VwcG9ydCBQcm9maWxlIl0sInNlYXJjaEh1YiI6IkV4dGVybmFsU2VhcmNoIiwidjgiOnRydWUsIm9yZ2FuaXphdGlvbiI6ImNvdmVvc2VhcmNoIiwidXNlcklkcyI6W3sicHJvdmlkZXIiOiJFbWFpbCBTZWN1cml0eSBQcm92aWRlciIsIm5hbWUiOiJhbm9ueW1vdXMiLCJ0eXBlIjoiVXNlciJ9XSwicm9sZXMiOlsicXVlcnlFeGVjdXRvciJdLCJzYWxlc2ZvcmNlQ29tbXVuaXR5IjoiaHR0cHM6XC9cL2NvdmVvY29tbXVuaXR5LmZvcmNlLmNvbVwvc3VwcG9ydFwvcyIsImV4cCI6MTUxODY0NDkyNywiaWF0IjoxNTE4NTU4NTI3LCJzYWxlc2ZvcmNlRmFsbGJhY2tUb0FkbWluIjp0cnVlLCJzYWxlc2ZvcmNlVXNlciI6InN1cHBvcnRAY292ZW9jb21tdW5pdHkuZm9yY2UuY29tIn0.h6Z-IkDyYc-eop6b7mdYeuIKOIe27z-p86uAK8oFPhw'}
NUMBER_OF_DOCUMENTS = 9288
MAXIMUM_NUMBER_OF_RESULTS = 1000
SMALLEST_ID = 4281000
BIGGEST_ID = 5549000


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


numberOfRequests = int((BIGGEST_ID - SMALLEST_ID) / MAXIMUM_NUMBER_OF_RESULTS)
printLine('\nNumber of requests planned : ' + str(numberOfRequests))
printLine('Starting requests to ' + URL + ' ...\n')

data = {'numberOfResults': str(MAXIMUM_NUMBER_OF_RESULTS), 'cq': ''}
for i in range(0, numberOfRequests):
	smallerId = SMALLEST_ID + MAXIMUM_NUMBER_OF_RESULTS * i
	biggerId = (SMALLEST_ID + MAXIMUM_NUMBER_OF_RESULTS * (i + 1)) + 1
	data['cq'] = '@sysrowid>' + str(smallerId) + ' AND @sysrowid<' + str(biggerId)
	response = requests.post(URL, headers=HEADERS, data=data)
	responseFile = open('responses/eachResponse/response' + str(i + 1) + '.txt', 'w')
	appendToFile(response.text, responseFile)
	printLine(str(i + 1) + '/' + str(numberOfRequests))
	
printLine('\nDone')