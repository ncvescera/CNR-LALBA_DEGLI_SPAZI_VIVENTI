#!/bin/bash

if ! dpkg -S `which pdftotext` > /dev/null; then
	sudo apt-get install poppler-utils -y
fi
