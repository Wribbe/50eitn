all: handin.pdf

handin.pdf: handin.tex create_schematics.py
	@python create_schematics.py
	@pdflatex handin.tex
