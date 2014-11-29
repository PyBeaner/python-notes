__author__ = 'pybeaner'

# false
print any([False, None, 0, 0L, 0.0, 0j, '', (), [], {}])
class C:
    # def __len__(self):
    #     return False
    def __nonzero__(self):
        return 0
if not C():
    print 'False'


# Numeric Types
import sys
print sys.maxint
print sys.float_info
# bit_length
n = 256
print n.bit_length(), bin(n)
# as_integer_ratio
print 1.1.as_integer_ratio()
# is_integer
print 1.0.is_integer()
print 1.20.hex()

# sequence types: str, unicode, list, tuple, bytearray, buffer, xrange
print []*3, [[]]*3
lists = [[]]*3
lists[0].append(1)
print lists, lists[0] is lists[1]
lists = [[] for i in range(3)]
lists[0].append(1)
print lists, lists[0] is lists[1]

# string
print 'abc'.capitalize()
print ' abc    '.center(40, '*')
# endswith(suffix of tuple of suffixes)
print 'abcdef'.endswith('def')
# find
print 'abc'.find('a') # index(-1 if not found)
# print 'abc'.index('e') # valueError if not found
print 'A Bc'.istitle()
print 'www.example.com'.lstrip('coxwz.')
# partition
print 'hello world'.partition(' ')
print 'hello world'.partition('  ')
# translate
import string
table = string.maketrans('aeiou', '12345')
print string.ascii_lowercase.translate(table, 'py')
# zfill
print 'abc'.zfill(5)
