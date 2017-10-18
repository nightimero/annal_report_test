# -*- coding:utf-8 -*-
class UrlGenerator(object):
    def __init__(self, root_url):
        self.url = root_url

    def __getattr__(self, item):
        if item == 'get' or item == 'post':
            print self.url
        else:
            print 'cannot find item:', self.url
        return UrlGenerator('{}/{}'.format(self.url, item))


url_gen = UrlGenerator('http://xxxx')
url_gen.users.show.get

# url_gen2 = UrlGenerator('http://xxxx')
# url_gen2.users.get.show
