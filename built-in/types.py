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