.PHONY: doc

all: history pack-doc pack

test:
	python test_math.py

test2:
	python test_string.py

doc: remove
	doxygen ./doc/Doxyfile

pack: remove
	zip -r xbabek01_xbarvi00_xmalan02_xsochu01.zip * .*

pack-doc: doc
	zip -r documentation.zip ./doc/html

remove:
	rm -rf ./doc/html *.pyc

history:
	git log --pretty=format:"%h - %an, %ar : %s" --all > history.txt

uninstall:
	sudo apt-get -remove thecalculator