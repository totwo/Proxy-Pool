# coding:utf-8
import re

import gevent

from fetcher import BaseFetcher


class Fetcher(BaseFetcher):
    name = 'CN_PROXY'
    enabled = False
    use_proxy = True

    def __init__(self, tasks, result, pool=None):
        super(Fetcher, self).__init__(tasks, result, pool)
        self.urls = [
            'https://cn-proxy.com/feed',
            'https://cn-proxy.com/archives/218'
        ]

    def handle(self, resp):
        return re.findall(r'((?:\d{1,3}\.){3}\d{1,3})</td>\s*<td>(\d+)</td>', resp.text)


if __name__ == '__main__':
    Fetcher.test()
