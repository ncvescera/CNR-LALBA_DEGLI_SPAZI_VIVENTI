#!/usr/bin/python

import os
import sys
import re

def pdf2txt(file):
	#conversione pdf to txt
	print "Parsing PDF file to txt ..."
	os.system("./ckutils.sh")
	os.system("pdftotext "+file+" out.txt")
	print "Done :D"

def getUpperWords(file):
	f = open(file,"r")
	rows = f.readlines()
	f.close()

	for row in rows:
		words = row.split(" ")
		for word in words:
			if word.istitle():
				#regular expression serve per cercare e sostituire un determinato set di caratteri
				regularExpression = re.compile('[^a-zA-Z]')
				print regularExpression.sub('',word)


pdf2txt(sys.argv[1]) #arg 1 passato allo scritp
getUpperWords("out.txt")