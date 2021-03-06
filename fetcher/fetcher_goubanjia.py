# coding:utf-8
import re

import gevent

from fetcher import BaseFetcher
from utils.functions import IPPortPatternGlobal


class Fetcher(BaseFetcher):
    name = 'goubanjia'

    def __init__(self, tasks, result, pool=None):
        super(Fetcher, self).__init__(tasks, result, pool)
        self.urls = [
            'http://www.goubanjia.com/'
        ]

    def handle(self, resp):
        html = re.sub(r"<p style='display:\s*none;'>\S*</p>", '', resp.text)
        html = re.sub(r'</?(span|div).*?>', '', html)
        return IPPortPatternGlobal.findall(html)


if __name__ == '__main__':
    Fetcher.test()
