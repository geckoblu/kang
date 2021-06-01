==============
Personal Notes
==============


Build environment
=================

pylint
------
pylint kang

pylint --disable=all --enable=line-too-long kang



tests
-----------------------
python3 -m unittest discover

python3 kang/gui/tests/testMainWindow.py TestMainWindow.test_populateText



code coverage
-----------------------

python3-coverage run -m unittest discover && python3-coverage html -i

python3-coverage run --source=kang -m unittest discover && python3-coverage html -i

python3-coverage run -m unittest kang/modules/tests/testRegexProcessor.py && python3-coverage html -i



Mime Type Setup
===============

sudo xdg-mime install --mode system data/kang-mimetype.xml

sudo xdg-icon-resource install --mode system --size 48 application-x-kang.png

sudo xdg-mime default kang.desktop application/x-kang

xdg-mime query filetype ./kng/pippo.kng
