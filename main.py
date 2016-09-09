#!/usr/bin/python

import os
import sys
import re
import geonames.adapters.search

from credential1 import *
from Country import *

dictionary = ["area","areas","located"]

def ckLib():
	print "Checking libraries ..."
	print "Check: poppler-utils ..."
	os.system("sudo apt-get install poppler-utils -y")

	print "Check: psycopg2 ..."
	os.system("sudo apt-get install python-psycopg2 -y")
	
	print "Check: geonames ..."
	os.system("sudo add-apt-repository ppa:ubuntugis/ppa -y -qq")
	os.system("sudo apt-get update -y -qq")
	
	print "Done :D"

def pdf2txt(file):
	#conversione pdf to txt
	print "Parsing PDF file to txt ..."
	os.system("pdftotext -l 4 "+file+" out.txt") #converte solo le prime 3 pagine
	print "Done :D"

def getUpperWords(file):
	f = open(file,"r")
	rows = f.readlines()
	f.close()

	upperWords = []

	for row in rows:
		words = row.split(" ")
		haveToAdd = False
		for word in words:
			if word == dictionary[0] or word == dictionary[1] or word == dictionary[2]:
				haveToAdd = True
				break
		if haveToAdd == True:
			for word in words:
				if word.istitle():
					#regular expression serve per cercare e sostituire un determinato set di caratteri
					regularExpression = re.compile('[^a-zA-Z]')
					upperWords.append(regularExpression.sub('',word))

	return upperWords #array di stringhe


def connectdb():
	import psycopg2

	print "Connecting to database ..."
	conn = psycopg2.connect("dbname="+dbname+" user="+user+" password="+password+" host="+host+" port="+port)
	if conn:
		return conn #oggetto connessione psycopg2
	else:
		return -1;

def matchWords(words,connection):
	print "Matching words ..." 

	cursor = connection.cursor()
	ids = []
	for word in words:
		cursor.execute("SELECT * FROM countries WHERE city = '"+word+"' ORDER BY id asc")
		result = cursor.fetchall()
		if len(result) > 0:
			for elem in result:
				print str(elem[0])+" " + elem[1] +" "+ elem[2][:-1] +" ---> " + word 
				ids.append(Country(elem[0],elem[1],elem[2][:-1]))

	print "Found "+str(len(ids))+" words\n"
	print "Optimazed match..."
	match = optimazedMatch(ids)
	print "Optimazed match succesful: found "+str(len(match))+" words\n"
	return match

def optimazedMatch(ids):
	newIds = []
	newIds.append(ids[0])

	for elem in ids:
		add = False
		for idN in newIds:
			if elem.city == idN.city:
				add = False
				break
			else:
				add = True

		if add == True:
			newIds.append(elem)

	return newIds

def fetchGeonames(matches):
	"""
	os.system("gn_search -p query malaysia -p max_rows 3 dsoprea > geonames.txt")
	"""
	pass

ckLib()

pdf2txt(sys.argv[1]) #arg 1 passato allo scritp
words = getUpperWords("out.txt")
words = list(set(words)) #elimina glie elementi dioppi
words.sort()
os.system("rm out.txt")

connection = connectdb()
if connection == -1:
	print "Error, connection faild !"
	exit()
print "Connection succesful :D"

matches = matchWords(words,connection)
for elem in matches:
	print elem.city + " "+ elem.nation

