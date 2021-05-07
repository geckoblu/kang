# pyuic4 -w mainWindowBA.ui > mainWindowBA.py

# pyrcc4 resources.qrc > modules/resources.py

VERSION = '5.0'

KANG_WEBSITE = 'http://www.geckoblu.net/kang'

PYTHON_RE_LIBRARY_URL = 'https://docs.python.org/3/library/re.html'

# match status
MATCH_NONE = -1
MATCH_NA = 0
MATCH_OK = 1
MATCH_FAIL = 2
MATCH_PAUSED = 3
MATCH_EXAMINED = 4

_ = lambda st: st  # No translation at the moment

MSG_NA = _("Enter a regular expression and a string to match against")
MSG_PAUSED = _("Kang regular expression processing is paused.  Click the pause icon to unpause")
MSG_FAIL = _("Pattern does not match")

MSG_MATCH_FOUND = _("Pattern matches (found 1 match)")
MSG_MATCHES_FOUND = _("Pattern matches (found %d matches)")
