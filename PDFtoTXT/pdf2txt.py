#!/usr/bin/python

import os

#file must be a string
def pdf2html(file):
	print "Converting pdf to html ..."
	os.system("java -jar PDFToHTML.jar "+file+" out.html")
	print "Done :D"
	print "Delating img tags ..."
	noimgs("out.html")
	print "Done :D"
#end function

def noimgs(file):
	array = list()
	
	with open(file,"r") as line:
		for temp in line:
			if "img" not in temp and "src" not in temp:
				array.append(temp)
				
	#end with
	
	docHtml = open("out.html","w")
	
	for row in array:
		docHtml.write(row)
	docHtml.close()
	
#end function noimgs
def nospaces(file):
	f = open(file,"r")
	lines = f.readlines()
	f.close()

	f = open(file,"w")
	for line in lines:
		f.write(line.replace(" ",""))
	f.close()

def html2txt(file):
	print "Parsing html to txt ..."

	os.system("./html2txt " + file)
	nospaces("../File/out.txt")
	os.system("rm " + file)
	
	print "Done :D"


pdf2html("../File/file.pdf")

html2txt("out.html")
