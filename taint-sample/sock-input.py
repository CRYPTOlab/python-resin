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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.set_taint(Taint(123))
s.__meta__ = "just testing"
s.connect(("kk.csail.mit.edu", 80))

s.send("GET / HTTP/1.0\r\n\r\n")
r = s.recv(128)
print r.__taint__.l
print r

s.close()

