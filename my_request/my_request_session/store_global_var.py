# -*- coding: utf-8 -*-
import requests
# 1.store global
s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print r.text

{"headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.9.1",
    "X-Test": "true",
    "X-Test2": "true"
  }
}

# 2. overide global var
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'false'})
print r.text

# 3. delete global var
r = s.get('http://httpbin.org/headers', headers={'x-test2': None})
print r.text