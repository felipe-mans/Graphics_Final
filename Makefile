file = cool.mdl
make: $(file) lex.py main.py matrix.py mdl.py script.py yacc.py
	python main.py $(file)
	convert ./anim/* animation.gif
	animate -delay 2.5 animation.gif

clean:
	rm *pyc *out parsetab.py
	rm ./anim/*

clear:
	rm *pyc *out parsetab.py *ppm

