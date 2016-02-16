==============
Personal Notes
==============


Build environment
=================

pylint
------
pylint -f html kang > ~/tmp/kang-pylint.html

tests and code coverage
-----------------------
nosetests




Mime Type Setup
===============

sudo xdg-mime install --mode system data/kang-mimetype.xml

sudo xdg-icon-resource install --mode system --size 48 application-x-kang.png

sudo xdg-mime default kang.desktop application/x-kang

xdg-mime query filetype ./kng/pippo.kng
