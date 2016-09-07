#!/usr/bin/python

import os

def pdf2txt(file):
	#conversione pdf to txt
	print "Parsing PDF file to txt ..."
	os.system("./ckutils.sh")
	os.system("pdftotext "+file+" out.txt")
	print "Done :D"

