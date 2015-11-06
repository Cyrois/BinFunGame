#!/usr/bin/python
from buffer import Buffer


#Test
if __name__ == '__main__':
    buf1 = Buffer("Nest 3rd Floor",1,2,3,4)
    print buf1.location
    print Buffer.__doc__
    print buf1.getCount("blue")
    for i in range(0,10):
        buf1.incrementCount("blue")
    print buf1.getCount("blue")