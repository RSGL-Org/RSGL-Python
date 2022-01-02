PYVER = 3.9

all:
	sudo cp RSGL.py /usr/lib/python$(PYVER)/site-packages/

local:
	cp RSGL.py ~/.local/lib/python$(PYVER)/site-packages/

install:
	sudo cp RSGL.py /usr/lib/python$(PYVER)/site-packages/

remove:
	sudo rm RSGL.py /usr/lib/python$(PYVER)/site-packages/