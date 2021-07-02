# KANG - The Python Regular Expression Editor

Kang is a Python GUI utility for editing, testing and debugging regular expressions for the Python programming language. 

Kang should aid any developer to efficiently and effortlessly develop regular expressions in Python. 
Since Python's implementation of regular expressions is based on the [PCRE](http://www.pcre.org/) standard, Kang should benefit developers in other programming languages that also adhere to the [PCRE](http://www.pcre.org/) standard (Perl, PHP, etc...).

## Screenshot

<img src="./screenshot.png?raw=true" alt="Screenshot" width="236"/>

## Install

Qt5 and PySide2 are required.  
Make sure that they are installed on your system.  

    # On Debian / Ubuntu
    sudo aptitude install python3-pyside2.qtwidgets
    
**From sources**

    sudo ./setup.py install # to install in the system
    sudo ./setup.py integrate_desktop # desktop integration

## Credits

Kang is a fork of [Kodos](http://kodos.sourceforge.net/).
Kodos seems to be abandoned and no longer maintained, it still uses Qt3 which were removed from all the major Debian distributions.
So after unsuccessfully try to contact the developer of Kodos I decided to start the porting to Qt4 myself.
So Kang is the porting of Kodos to Qt4, plus the changes I decided to do during the way.

**UPDATE**: After a few years in which I also abandoned Kang, I now found the time to work on it.
Qt4 is now obsolete and I was forced to port Kang to Qt5, during the porting I decided to switch from PyQt4 to PySide2. I plan to port Kang to Qt6 as soon as possible (read when PySide6 will land in Debian)

## License
Kang is an open source project released under the [GNU Public License (GPL) v2](http://www.gnu.org/licenses/gpl-2.0.txt).
