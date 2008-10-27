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
	pass

def pt(s):
    print s
    print s.__taint__.l

x = "abc".taint(Taint(5))
y = "def".taint(Taint(6))
z = "ghi".taint(Taint(7))

x2 = "abc".taint(Taint(105))
y2 = "def".taint(Taint(106))
z2 = "ghi".taint(Taint(107))

pt(x+y)
pt(x2+y)
pt(x+z)
pt(x+z2)

a=x+y+z
pt(a)

b=x+y
c=b+z
pt(c)

