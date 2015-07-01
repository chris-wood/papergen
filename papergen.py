# File: paper_gen.py 
# Author: Quickly generate a new paper template using the standard style

import sys
import argparse
import os
import shutil
from subprocess import call

# Useful little tool for touching the bibliography
def _touch(fname):
    if os.path.exists(fname):
        os.utime(fname, None)
    else:
        open(fname, 'w').close()

def touch(fname):
	call(["touch", fname])

# Specify arguments
parser = argparse.ArgumentParser(description='Generate a new paper.')
parser.add_argument('--title', type=str, help='Title of the paper', required = True)
parser.add_argument('--year', type=int, help='Year of the paper', required = True)
parser.add_argument('--name', type=str, help='Full name of primary author', required = True)
parser.add_argument('--email', type=str, help='Email address of the primary author', required = True)

# TODO: expand the generic paper generator thing to support more modes
# TODO: add options for ACM/IEEE/Elsevier and whatnot

# Parse the arguments
args = parser.parse_args()
title = args.title
year = args.year
name = args.name
email = args.email

# Abbreviate for the directory and file name
names = name.split(" ")
lastName = names[len(names) - 1]
titleWords = title.split(" ")
titleAbbrv = ""
for w in titleWords:
	titleAbbrv = titleAbbrv + w[0:1].upper()

dirName = titleAbbrv.replace(" ", "") + "_" + lastName.replace(" ","") + "_" + str(year)
print("Checking for directory: " + dirName)
if not os.path.exists(dirName):
	print("Creating and dumping new content")
	os.makedirs(dirName)

	# Touch the bib file
	touch(dirName + os.sep + dirName + ".bib")

	# Copy template into the directory
	# TODO: switch here on the type of template we're copying into the directory
	tmp = open("templates/generic_template.tex", 'r')
	target = open(dirName + os.sep + dirName + ".tex", 'w')
	lines = []
	for l in tmp:
		if ("--NAME--" in l):
			l = l.replace("--NAME--", name)
		if ("--YEAR--" in l):
			l = l.replace("--DATE--", year)
		if ("--EMAIL--" in l):
			l = l.replace("--EMAIL--", email)
		if ("--TITLE--" in l):
			l = l.replace("--TITLE--", title)
		if ("--ABBRV--" in l):
			l = l.replace("--ABBRV--", dirName)
		target.write(l)

	# Copy Makefile into the directory
	tmp = open("templates/Makefile_template", 'r')
	target = open(dirName + os.sep + "Makefile", 'w')
	lines = []
	for l in tmp:
		if ("--TITLE--" in l):
			l = l.replace("--TITLE--", dirName)
		# lines.append(l)
		target.write(l)

	# Copy the style file over
	shutil.copyfile("templates/cawsty.sty", dirName + os.sep + "cawsty.sty")
		
	# Done.
	print("Paper generation complete. See " + dirName + " for contents")
else:
	print("Error: directory already exists. Not overwriting your work.")

