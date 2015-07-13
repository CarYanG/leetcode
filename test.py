__author__ = 'carl'
import sys
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a=34342

print type(a)
a=ListNode(None)


str_lists=[[]for i in range (3)]
print str_lists

a='123'
b='234'
a=list(a)
b=list(b)
a.extend(b)
print ''.join(a)
print sys.maxint

a=123
c=list(str(a))
c.reverse()
print c

a='123'
b=int(a)
print type(b)
print int('1')

aa={}
b=[1,1,1,1,1]
for i in range(len(b)):
    aa[i]=b[i]

print aa
print aa.keys()
print len(aa.keys())

a=[1,5,3]
a.reverse()
print a
print a[0]
print max(a),min(a)

s='   as  ada   dasd'
print s.strip()
ss=s.strip().split(" ")
print ss






