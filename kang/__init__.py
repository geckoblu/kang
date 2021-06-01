
VERSION = '5.0'

KANG_WEBSITE = 'https://github.com/geckoblu/kang'

PYTHON_RE_LIBRARY_URL = 'https://docs.python.org/3/library/re.html'

# match status
MATCH_NONE = -1
MATCH_NA = 0
MATCH_OK = 1
MATCH_FAIL = 2
MATCH_PAUSED = 3
MATCH_EXAMINED = 4

tr = lambda st: st  # No translation at the moment

MSG_NA = tr("Enter a regular expression and a string to match against")
MSG_PAUSED = tr("Kang regular expression processing is paused.  Click the pause icon to unpause")
MSG_FAIL = tr("Pattern does not match")

MSG_MATCH_FOUND = tr("Pattern matches (found 1 match)")
MSG_MATCHES_FOUND = tr("Pattern matches (found %d matches)")
