from PyQt4.QtCore import QFile, QTextStream, QIODevice
import os
import re

from kang.modules.util import findFile


rx_entry = re.compile(r"<entry>(?P<content>.*?)</entry>", re.DOTALL)
rx_desc = re.compile(r"<desc>(.*)</desc>", re.DOTALL)
rx_regex = re.compile(r"<regex>(.*)</regex>", re.DOTALL)
rx_tab = re.compile(r"<tab>(.*)</tab>", re.DOTALL)
rx_text = re.compile(r"<text>(.*)</text>", re.DOTALL)
rx_note = re.compile(r"<note>(.*)</note>", re.DOTALL)
rx_contrib = re.compile(r"<contrib>(.*)</contrib>", re.DOTALL)
rx_replace = re.compile(r"<replace>(.*)</replace>", re.DOTALL)

RX_DICT = {'desc': rx_desc,
           'regex': rx_regex,
           'tab': rx_tab,
           'text': rx_text,
           'note': rx_note,
           'contrib': rx_contrib,
           'replace': rx_replace}


class ParseRegexLib:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), 'regex-lib.xml')
        if path:
            f = QFile(path)
            f.open(QIODevice.ReadOnly | QIODevice.Text)
            self.data = QTextStream(f).readAll()
            f.close()

    def parse(self, data=""):
        if not data:
            data = self.data

        dicts = []
        allmatches = rx_entry.findall(data)
        rx_keys = RX_DICT.keys()
        for match in allmatches:
            d = {}
            for key in rx_keys:
                m = RX_DICT[key].search(match)
                if m:
                    d[key] = m.group(1)
                else:
                    d[key] = ""

            dicts.append(d)

        return dicts
