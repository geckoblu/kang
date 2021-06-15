class FakeWebbrowser():

    def __init__(self):
        self._url = ''

    def open(self, url):
        self._url = url

    # def assertIsLocalUrl(self, testcase):
    #     res = self._url.startswith('file://')
    #     testcase.assertTrue(res, 'URL isn\'t local: %s' % self._url)

    def assertIsWebUrl(self, testcase):
        res = self._url.startswith('http://') or self._url.startswith('https://')
        testcase.assertTrue(res, 'URL isn\'t Web: %s' % self._url)
