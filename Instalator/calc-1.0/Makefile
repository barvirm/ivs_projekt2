DEBEMAIL='xbabek01@stud.fit.vutbr.cz'

All:

setup: rm_old dhmake rm_ex


rm_old:
	rm -rf debian/ ../calc_*

dhmake:
	dh_make -c gpl -e $(DEBEMAIL) --createorig 

rm_ex:
	rm -rf debian/*.ex debian/*.EX

dpkg:
	dpkg-buildpackage
