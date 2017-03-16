
import requests
import json

def request(title):
	try:
		req = requests.get('http://www.omdbapi.com/?t=' + title)
		dictionary = json.loads(req.text)
		return dictionary
	except:
		print('Connection Error')

def display(movie):
	print('Title:', movie['Title'])
	print('Released:', movie['Released'])
	print('Director:', movie['Director'])
	print('Actors:', movie['Actors'])
	print('Poster:', movie['Poster'])

exit = False
while not exit:
	op = input('Title or 0 to EXIT:')
	movie = request(op)
	if op == '0':
		exit = True
	else:
		display(movie)