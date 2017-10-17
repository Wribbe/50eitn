all: handin.pdf frame.pdf

handin.pdf : handin.tex create_table.py
	@python create_table.py
	@pdflatex $^

frame.pdf : frame.tex
	@pdflatex $^
