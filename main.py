#!/usr/bin/python

import os
import sys
import re
import psycopg2

from credential import *

def pdf2txt(file):
	#conversione pdf to txt
	print "Parsing PDF file to txt ..."
	os.system("sudo apt-get install poppler-utils -y")
	os.system("pdftotext "+file+" out.txt")
	print "Done :D"

def getUpperWords(file):
	f = open(file,"r")
	rows = f.readlines()
	f.close()

	upperWords = []

	for row in rows:
		words = row.split(" ")
		for word in words:
			if word.istitle():
				#regular expression serve per cercare e sostituire un determinato set di caratteri
				regularExpression = re.compile('[^a-zA-Z]')
				upperWords.append(regularExpression.sub('',word))

	return upperWords #array di stringhe

def connectdb():
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
		cursor.execute("SELECT * FROM countries WHERE city = '"+word+"'")
		resutl = cursor.fetchall()
		if len(result) > 0:
			for elem in resutl:
				ids.appen(elem[0])

	print "Found "+str(len(ids))+" words"
	
	return ids #array di interi

pdf2txt(sys.argv[1]) #arg 1 passato allo scritp
words = getUpperWords("out.txt")
os.system("rm out.txt")

connection = connectdb()
if connection == -1:
	print "Error, connection faild !"
	exit()
print "Connection succesful :D"

matchWords(words,connection)


