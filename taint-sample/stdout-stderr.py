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

x = "abc"
y = "secret".taint(Taint(5))

print "x to stdout:", x
try:
    print "y to stdout:", y
except:
    print "Could not print y to stdout"

try:
    print >>sys.stderr, "y to stderr:", y
except:
    print "Could not print y to stderr"

print "untainted y to stdout:", y.taint(None)

