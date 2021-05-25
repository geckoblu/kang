# pylint: disable=line-too-long

REGEXLIBRARY = [
    {
        'desc': 'Locate all words in a string',
        'note': '',
        'tab': 0,
        'match': 'Here  you will find several   words seperated by    whitespace.\n\nUse the \'Match Number\' spinbox to cycle through the matches.',
        'regex': '(?P<word>\\w*?)\\W+',
        'replace': '',
        'contributor': 'Phil Schwartz'
    },
    {
        'desc': 'Replace a word in a string',
        'note': '',
        'tab': 2,
        'match': 'this example replaces the WORD in this string',
        'regex': '(?P<word>WORD)\\W+',
        'replace': '__replacement__',
        'contributor': 'Phil Schwartz'
    },
    {
        'desc': 'Find dates in the form Month day, year (eg. January 10, 2003)',
        'note': 'Suitable for most purposes, however, it may be necessary for the user to validate that the day exists in the month (and in the case of February, the year as well).',
        'tab': 0,
        'match': 'Here is a date: Feb 12, 2003.  This example does not determine if the month actually has the number of days listed.  So it will incorrectly match Feb 31, 2003.',
        'regex': '(?i)(?P<month>january|jan|february|feb|march|mar|april|apr|may|june|jun|july|jul|august|aug|september|sep|october|oct|november|nov|december|dec)\\s+(?P<day>3[01]|[0-2]{0,1}\\d),\\s*(?P<year>\\d{4})\\W*',
        'replace': '',
        'contributor': 'Phil Schwartz'
    },
    {
        'desc': 'Extract the BODY section from an HTML string',
        'note': '',
        'tab': 0,
        'match': '<HTML><HEAD><TITLE>test</TITLE></HEAD><BODY>This is an example of extracting the BODY from an HTML string</BODY></HTML>',
        'regex': '(?si)<body>(?P<contents>.*)</body>',
        'replace': '',
        'contributor': 'Phil Schwartz'
    },
    {
        'desc': 'Strip HTML tags from string',
        'note': 'Primitive example - The replace string is a single space',
        'tab': 2,
        'match': '<html><head><title>test</title></head><body>test of replacing html tags</body></html>',
        'regex': '(?is)<.*?>',
        'replace': ' ',
        'contributor': 'Phil Schwartz'
    },
    {
        'desc': 'Replace everything except the contents of BODY section from HTML',
        'note': 'Primitive example - The replace string is a single space.\nAssumes that the string is in the form:\n<HTML>...<HEAD>...</HEAD>...<BODY>....</BODY>...</HTML>',
        'tab': 2,
        'match': '<html><head><title>test</title></head><body>test of replacing opening and closing html tags.  All that should be left is this string.</body></html>',
        'regex': '(?is)(<html>.*<head>.*</head>.*<body>)|(</body>.*</html>)',
        'replace': ' ',
        'contributor': 'Phil Schwartz'
    }
]
