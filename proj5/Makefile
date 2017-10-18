inputs=$(foreach file,$(shell ls input),input/$(file))

all: handin.pdf frame.pdf

handin.pdf : handin.tex create_table.py $(inputs)
	@python create_table.py
	@pdflatex $^

frame.pdf : frame.tex
	@pdflatex $^
