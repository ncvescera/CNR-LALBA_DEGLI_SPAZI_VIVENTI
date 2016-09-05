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

pdf2html("file.pdf")
os.system("./HtmL out.html")

