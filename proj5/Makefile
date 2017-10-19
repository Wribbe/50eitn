inputs=$(foreach file,$(shell ls input),input/$(file))

all: handin.pdf frame.pdf

handin.pdf : handin.tex create_table.py generate_rational_matrix.py $(inputs)
	@python create_table.py
	@python generate_rational_matrix.py
	@pdflatex $^

frame.pdf : frame.tex
	@pdflatex $^
