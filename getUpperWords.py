#!/usr/bin/python
def getUpperWords(file):
	f = open(file,"r")
	rows = f.readlines()
	f.close()

	for word in rows:
		if word.istitle():
			print word

getUpperWords("testo.txt")