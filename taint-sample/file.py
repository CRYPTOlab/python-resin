#!/home/nickolai/python/taint-2.6/python
import os
import sys

class Taint:
    def __init__(self, *l):
	self.l = []
	self.l.extend(l)

    def merge(self, other):
	n = Taint()
	n.l.extend(self.l)
	n.l.extend(other.l)
	return n

    def export_check(self, f):
	print "export_check, taint =", self.l
	if (f is sys.stdout):
	    pass
	else:
	    raise Exception

x = "abc\n"
y = "secret\n".taint(Taint(5))

f = open("/tmp/python.out", "w")
f.write(x)

try:
    f.write(y)
except:
    print "Could not write y to file"

try:
    f.writelines((y))
except:
    print "Could not writelines y to file"

f.close()

