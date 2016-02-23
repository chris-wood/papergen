#!/bin/bash

#aspell -t -c file.tex

latex $1.tex
bibtex $1
latex $1.tex 
latex $1.tex
dvips $1.dvi
ps2pdf $1.ps

