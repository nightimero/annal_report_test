# -*- coding: utf-8 -*-
# !/user/bin/env python
# -*- coding: cp936 -*-
import time
from win32com.client import Dispatch

urlFileName = "urlFile.txt"
outputFileName = "result.txt"
outputFile = open(outputFileName, 'w')
ie = Dispatch("InternetExplorer.Application")
ie.visible = 1
ie.navigate('http://www.google.com.hk')
while (ie.ReadyState != 4):
    time.sleep(1)
print 'Ò³ÃæÔØÈëÍê½á'
with open(urlFileName) as urlFile:
    for url in urlFile:
        url = url.strip()
        ie.Document.forms[0].elements["q"].value = "site:" + url
        ie.Document.forms[0].submit()

        while (ie.ReadyState != 4 or str(ie.LocationURL).find(url) == -1):
            print str(ie.LocationURL)
            time.sleep(1)
        result = ie.Document.getElementById("ires").innerHTML
        if len(result) > 0:
            print url, "recored"
            outputFile.write(url + ":recored/n")
        else:
            print url, "not recored"
            outputFile.write(url + ":not recored/n")
outputFile.close()
