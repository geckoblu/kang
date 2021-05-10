import os
import re

from PySide2.QtCore import QFile, QTextStream, QIODevice

_RX_ENTRY = re.compile(r"<entry>(?P<content>.*?)</entry>", re.DOTALL)

_RX_DICT = {'desc': re.compile(r"<desc>(.*)</desc>", re.DOTALL),
            'regex': re.compile(r"<regex>(.*)</regex>", re.DOTALL),
            'tab': re.compile(r"<tab>(.*)</tab>", re.DOTALL),
            'text': re.compile(r"<text>(.*)</text>", re.DOTALL),
            'note': re.compile(r"<note>(.*)</note>", re.DOTALL),
            'contrib': re.compile(r"<contrib>(.*)</contrib>", re.DOTALL),
            'replace': re.compile(r"<replace>(.*)</replace>", re.DOTALL)
           }


class ParseRegexLib:

    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), 'regex-lib.xml')
        if os.path.isfile(path):
            try:
                f = QFile(path)
                f.open(QIODevice.ReadOnly | QIODevice.Text)
                self.data = QTextStream(f).readAll()
            finally:
                if f:
                    f.close()

    def parse(self, data=""):
        if not data:
            data = self.data

        dicts = []
        allmatches = _RX_ENTRY.findall(data)
        rxKeys = _RX_DICT.keys()
        for match in allmatches:
            d = {}
            for key in rxKeys:
                m = _RX_DICT[key].search(match)
                if m:
                    d[key] = m.group(1)
                else:
                    d[key] = ""

            dicts.append(d)

        return dicts
