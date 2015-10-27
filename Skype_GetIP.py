#!/usr/bin/env python
import sys
import urllib2
from MaltegoTransform import *

mt = MaltegoTransform()
mt.parseArguments(sys.argv)
SearchString = mt.getValue()
mt = MaltegoTransform()

url = 'http://api.predator.wtf/resolver/?arguments='+SearchString
ipaddress = urllib2.urlopen(url).read()
mt.addEntity("maltego.IPv4Address",ipaddress)
mt.returnOutput()