.PHONY: doc

all: pack-doc pack

test:
	python test_math.py

test2:
	python test_string.py

doc: remove
	doxygen ./doc/Doxyfile

pack: remove
	zip -r xbabek01_xbarvi00_xmalan02_xsochu01.zip *

pack-doc: doc
	zip -r documentation.zip ./doc/html

remove:
	rm -rf ./doc/html *.pyc

uninstall:
	sudo apt-get -remove thecalculator