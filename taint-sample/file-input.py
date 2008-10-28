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

f = open("/etc/passwd", "r");
f.set_taint(Taint(123))

s = f.read(128)
print s.__taint__.l

s = f.readline()
print s.__taint__.l

s = f.readlines()
print s[0].__taint__.l

f.close()

