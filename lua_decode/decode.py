# -*- coding:utf8 -*-
__author__='pcat@chamd5.org'
__blog__='http://pcat.cc'

from ctypes import *
import sys

def decrypt(filename):
    s=open(filename,'rb').read()
    outfile='decode_'+ filename
    if s[0]==chr(0x1b) and s[1]!=chr(0x4c):
        rst=chr(0x1b)
        size=len(s)
        v10=0
        for i in range(1,size):
            v10+=size
            v=(c_ulonglong(-2139062143*v10).value>>32)+v10
            v1=c_uint(v).value>>7
            v2=c_int(v).value<0
            rst+=chr(ord(s[i])^(v10+v1+v2)&0xff)
        with open(outfile,'wb') as f:
            f.write(rst)
    else:
        pass

def foo():
    if len(sys.argv)==2:
        filename=sys.argv[1]
    else:
        filename='main.lua'
    decrypt(filename)

if __name__ == '__main__':
    foo()
