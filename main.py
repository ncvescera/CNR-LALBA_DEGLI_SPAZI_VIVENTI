#!/usr/bin/python
 # -*- coding: UTF-8 -*-
import os
import sys
import re

from credential1 import *
from Country import *
from firstTime import *

dictionary = ["area","areas","located"]

def ckLib(firstTime):
	if firstTime:
		print "Checking libraries ..."
		print "Check: poppler-utils ..."
		os.system("./ckPkg.sh poppler-utils")

		print "Check: psycopg2 ..."
		os.system("./ckPkg.sh python-psycopg2")

		print "Check geonames ..."
		os.system("./installGeon.sh")

		print "Done :D"

		f = open("firstTime.py","w")
		f.write("#!/usr/bin/python\n")
		f.write("firstTime = False")
		f.close
		
		

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
	if len(words) > 0:
		print "Optimazed match..."
		match = optimazedMatch(ids)
		print "Optimazed match succesful: found "+str(len(match))+" words\n"
		return match
	else:
		return []

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
	import geonames.adapters.search
	geon = []
	_USERNAME = 'dsoprea'
	
	for match in matches:
		sa = geonames.adapters.search.Search(_USERNAME)
		result = sa.query(match.city).max_rows(3).execute()
		for id_, name in result.get_flat_results():
			geon.append(geonames.compat.make_unicode("{0},{1}").format(id_, name))

	end = []
	for match in matches:
		for elem in geon:
			temp = elem.split(",")
			if temp[1] == match.city:
				end.append(match.city)
				break
	last = []
	i=0
	for elem in end:
		i=i+1
		j=i
		for j in range(j,len(end)):
			sa = geonames.adapters.search.Search(_USERNAME)
			result = sa.query(elem+","+end[j]).max_rows(1).execute()
			for id_, name in result.get_flat_results():
				last.append(geonames.compat.make_unicode("{0}, {1}").format(id_, name))
	i=0
	toReturn = []
	for elem in last:
		add = True
		i=i+1
		j=i
		for j in range(j,len(last)):
			if elem ==last[j]:
				add = False
		if add == True:
			toReturn.append(elem)
	return toReturn

ckLib(firstTime)

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
if len(matches) > 0:
	print "Final matches: "
	matches = fetchGeonames(matches)
	for elem in matches:
		print elem 
else:
	exit(1)


