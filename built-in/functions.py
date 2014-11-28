__author__ = 'pybeaner'

# abs(x) if x is a complex number,return its magnitude
print abs(1),abs(-1),abs(1+1j)

# all(iterable) :Return True if all elements of the iterable are true
it_with_zero, it_without_zero, it_empty = [1,2,0], [1,2,3], []
print all(it_with_zero), all(it_without_zero), all(it_empty)

# any(iterable) :Return True if any element of the iterable is true
print any(it_with_zero), any(it_without_zero), any(it_empty)

# basestring:str and unicode
print isinstance('', basestring)

# bin(x): return binary string of x(or __index__() of x)
print bin(20)

# bool([x])
print bool(1), bool()
print issubclass(bool, int)

# class bytearray([source[,encoding[,errors]]])
# int
print bytearray(5)
# unicode(encoding is required)
print bytearray(u'china', 'utf-8')
# TODO: buffer
# iterable
print bytearray('123'), bytearray(['1','2','3']) ,bytearray([1,2,3])
# no source
print len(bytearray())

# callable(object):classes are callable (calling a class returns a new instance);
# class instances are callable if they have a __call__() method.
print callable(1), callable(int)

# chr(i): inverse of ord()
print chr(97), ord('a')
# unichr()
print unichr(255)

# classmethod
class C:
    attr1 = 1
    @classmethod
    def f(cls, n):
        print cls
        print n
    def f2(self, n):
        print n
print C.f(1), C().f(2)
print C().f2(3), C.f2(C(), 4)

# cmp(x, y)
print cmp(1, -3), cmp(-1, 2), cmp(0, False)

# compile(source, filename, mode[, flags, [dont_inherit]])
c = compile(source='import this', filename='a', mode='exec')
exec c

# class complex([real[, imag]])
print complex('1+2j')
# print complex('1 + 2j') #-->malformed string

# delattr(object, name)
print C.attr1
delattr(C, 'attr1') # del C.attr1

# dir([object])
print dir()
import struct
print dir(struct)
class Dir:
    def __dir__(self):
        return ['hello', 'world']
print dir(Dir())

# divmod(x, y)
print divmod(100, 3), divmod(12.0, 2.0)

# enumerate(sequence, start=0)
l = [1,2,3]
print list(enumerate(l)), list(enumerate(l, start=1))

# eval()

# filter()
print filter(lambda x:x, [1,0,None,True])

# hash
print hash(1), hash(1.0), hash(__file__)

# hex
print hex(256), int('0x100', base=16)

# isinstance()
print isinstance(int, type), isinstance(1, int)

# map()
def f(x):
    return x+1
print map(f, [1,2,3])
def f2(x,y):
    return x+y
print map(f2, [1,2,3], [2,3,4])
# print map(f2, [1,2,3], [2,3])#==>None

# pow(x, y, z)
print pow(2, 3)