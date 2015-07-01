FNAME=fname

all:
	pdflatex ${FNAME}.tex
	bibtex ${FNAME}
	pdflatex ${FNAME}.tex
	pdflatex ${FNAME}.tex

clean:
	rm ${FNAME}.pdf *.aux *.log *.bbl
