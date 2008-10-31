#!/home/nickolai/python/taint-2.6/python
import os
import sys
import cStringIO

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
	pass

def pt(s):
    print s
    print s.__taint__
    print s.__taint__.l

x = "abc\ndef\n".taint(Taint(5))
y = "def".taint(Taint(6))
z = "ghi".taint(Taint(7))

f = cStringIO.StringIO(x)

x2 = f.read(3)

pt(x)
pt(x2)

f2 = cStringIO.StringIO()

f2.write(y)
f2.write(z)
f2.reset()
yz2 = f2.readline()

pt(yz2)

