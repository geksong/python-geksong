# -*- coding: utf-8 -*-
import urllib
import sys

host = sys.argv[1]
f = urllib.urlopen(host)
while 1:
	buf = f.read(2048)
	if not len(buf):
		break
	print buf