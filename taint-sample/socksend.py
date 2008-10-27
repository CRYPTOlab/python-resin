#!/home/nickolai/python/taint-2.6/python
import os
import sys
import socket

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("kk.csail.mit.edu", 80))

s.send(x)
try:
    s.send(y)
except:
    print "Could not send y to socket"

try:
    s.sendall(y)
except:
    print "Could not sendall y to socket"

try:
    s.sendto(y, ("1.2.3.4", 1234))
except:
    print "Could not sendto y to socket"

s.close()

