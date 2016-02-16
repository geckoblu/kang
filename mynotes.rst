Personal Notes
==============



Mime Type Setup
---------------

sudo xdg-mime install --mode system data/kang-mimetype.xml

sudo xdg-icon-resource install --mode system --size 48 application-x-kang.png

sudo xdg-mime default kang.desktop application/x-kang

xdg-mime query filetype ./kng/pippo.kng
