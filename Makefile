.PHONY: doc

test:
	python test_math.py

test2:
	python test_string.py

doc:
	doxygen ./doc/Doxyfile

pack: remove
	zip xbabek01_xbarvi00_xmalan02_xsochu01.zip *

remove:
	rm -rf ./doc/html *.pyc *.zip